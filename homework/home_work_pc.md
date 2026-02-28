```java
This is my eve-ng : http://192.168.187.135/legacy/VXLAN%20EVPN%20FABRIC-IPSEC%20-MPLS%20VPN.unl/topology

Topology Details: 
Management(cloud0) is connected to eth5 HANA-SW
Management(cloud0) is connected to eth9 STR-SW
Note: Both are access Arista Veos 8.0.1 swithes

Management(cloud0) is connected to eth8 LEAF-1
Management(cloud0) is connected to eth8 LEAF-2
Note: Both are border leaf- Arista Veos 8.0.1 swithes

Management(cloud0) is connected to eth1 LEAF-3
Management(cloud0) is connected to eth1 LEAF-4
Note: Both are border leaf- Arista Veos 8.0.1 swithes

Management(cloud0) is connected to eth1 Spine-1
Management(cloud0) is connected to eth1 Spine-2
Note: Both are spines leaf- Arista Veos 8.0.1 swithes & connected with all LEAF-1,2,3,4

Management(cloud0) is connected to eth1 WAN-1
Management(cloud0) is connected to eth1 WAN-2
Note: Both are border leaf- CISCO CSR1000v

GitHub URL: https://github.com/Jeet905122593/JEET_ROY/edit/main/Cisco-vrf-aware-ipsec-vpn.md
Rep: https://github.com/Jeet905122593/JEET_ROY.git

IP Plan
🔷 Spine Layer
Device	Mgmt Interface	IP
Spine-1	eth1	192.168.187.201
Spine-2	eth1	192.168.187.202
🔷 Border Leaf
Device	Mgmt	IP
LEAF-1	eth8	192.168.187.211
LEAF-2	eth8	192.168.187.212
🔷 Leaf
Device	Mgmt	IP
LEAF-3	eth1	192.168.187.213
LEAF-4	eth1	192.168.187.214
🔷 Access Switch
Device	Mgmt	IP
HANA-SW	eth5	192.168.187.221
STR-SW	eth9	192.168.187.222
🔷 WAN (CSR1000v)
Device	Mgmt	IP
WAN-1	eth1	192.168.187.231
WAN-2	eth1	192.168.187.232
==================================================================================================
conf t
  interface ethernet 9
  no shutdown
  no switchport
  ip add 192.168.187.222 255.255.255.0
  exit
username admin privilege 15 secret admin
management ssh
 no shutdown
write memory
==================================================================================================
i
======================================================================
step-1:

Before installing anything, tell Ubuntu to refresh its list of available software.

sudo apt update
sudo apt upgrade -y
sudo apt install git -y
sudo apt install python3-pip python3-venv -y
sudo apt install python3-paramiko -y
=> to check need to run : python3 -c "import paramiko; print('Paramiko OK')"

cd ~
git clone https://github.com/Jeet905122593/JEET_ROY.git  ( to Fetch with GitHub repo)
cd JEET_ROY
ls

ssh admin@192.168.187.221
ssh admin@192.168.187.222
==============For devices====================
conf t
  interface ethernet 9
  no shutdown
  no switchport
  ip add 192.168.187.222 255.255.255.0
  exit
username admin privilege 15 secret admin
management ssh
 no shutdown
write memory
==================================
From scratch/power off Ubuntu VM, we need to cd ~/JEET_ROY 
Note1: 
If you want to go Inventory then cd ~/JEET_ROY/basic-automation/inventory
If you need remove any file  rm -r hosts.ini
To check in the folder ls -l or ls
To fetch with GitHub to VSCODE:
cd ~/JEET_ROY
code .


jeet@jeet-VMware-Virtual-Platform:~$ cd ~/JEET_ROY
jeet@jeet-VMware-Virtual-Platform:~/JEET_ROY$ mkdir basic-automation
jeet@jeet-VMware-Virtual-Platform:~/JEET_ROY$ cd basic-automation
jeet@jeet-VMware-Virtual-Platform:~/JEET_ROY/basic-automation$ mkdir inventory playbooks templates vars output
jeet@jeet-VMware-Virtual-Platform:~/JEET_ROY/basic-automation$ ls
inventory  output  playbooks  templates  vars



Note2: Make sure you will create file & write something.
### To Check changes
git status

### To Add
git add 

### To Commit
git commit -m "Describe what you changed"

### To Push
git push origin main

