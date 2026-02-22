import yaml
import subprocess
import os

# # Project root path বের করা
# base_dir = os.path.dirname(os.path.dirname(__file__))

# # inventory file path তৈরি করা
# inventory_path = os.path.join(base_dir, "inventory", "devices.yaml")

# # YAML load করা
# with open(inventory_path) as file:
#     data = yaml.safe_load(file)

# def ping_device(ip):
#     result = subprocess.run(
#         ["ping", "-n", "2", ip],  # Windows
#         capture_output=True,
#         text=True
#     )

#     if "Reply from" in result.stdout:
#         return True
#     return False

# # Loop করে সব device ping করা
# for device in data["devices"]:
#     print(f"Pinging {device['name']} ({device['host']})")

#     if ping_device(device["host"]):
#         print("✅ Reachable\n")
#     else:
#         print("❌ Not reachable\n")

# import yaml
# import os
# from netmiko import ConnectHandler

# # Project root path
# base_dir = os.path.dirname(os.path.dirname(__file__))
# inventory_path = os.path.join(base_dir, "inventory", "devices.yaml")

# # Load YAML
# with open(inventory_path) as file:
#     data = yaml.safe_load(file)

# # Loop through devices
# for device in data["devices"]:
#     print(f"\nConnecting to {device['name']} ({device['host']})")

#     try:
#         connection = ConnectHandler(
#             device_type=device["device_type"],
#             host=device["host"],
#             username=device["username"],
#             password=device["password"],
#         )

#         output = connection.send_command("show version")
#         print("✅ SSH Success")
#         print(output)

#         connection.disconnect()

#     except Exception as e:
#         print("❌ SSH Failed")
#         print(e)

import yaml
import os
from netmiko import ConnectHandler
from jinja2 import Environment, FileSystemLoader

# Project base path
base_dir = os.path.dirname(os.path.dirname(__file__))

# Inventory path
inventory_path = os.path.join(base_dir, "inventory", "devices.yaml")

# Template loader
env = Environment(loader=FileSystemLoader(os.path.join(base_dir, "templates")))
template = env.get_template("vlan_template.j2")

# Load inventory
with open(inventory_path) as file:
    data = yaml.safe_load(file)

# Loop devices
for device in data["devices"]:
    print(f"\nConnecting to {device['name']} ({device['host']})")

    try:
        connection = ConnectHandler(
            device_type=device["device_type"],
            host=device["host"],
            username=device["username"],
            password=device["password"],
        )

        # Render template
        config = template.render(
            vlan_id=device["vlan_id"],
            vlan_name=device["vlan_name"]
        )

        print("Generated Config:")
        print(config)

        # Push config
        output = connection.send_config_set(config.split("\n"))
        print(output)

        connection.disconnect()
        print("✅ VLAN Config Pushed Successfully")

    except Exception as e:
        print("❌ Failed")
        print(e)