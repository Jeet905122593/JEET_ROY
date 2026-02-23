```java

1. ✅ Basic Linux checks
2. ✅ Networking checks
3. ✅ Commands needed for Network Automation
4. ✅ Generate SSH Key
5. ✅ Run Ansible ping
---

# 🔹 PART 1 — Basic Linux Commands (Daily Use)
---
## 1️⃣ `pwd`

**What it does:**
Shows your current location (folder).

```bash
pwd
```

**Purpose:**
To know where you are before creating or running files.

**Use Case (Automation):**
Before running `ansible-playbook`, confirm you're inside project folder.

---

## 2️⃣ `ls`

**What it does:**
Shows files in current folder.

```bash
ls
ls -l
ls -a
```

* `-l` → detailed view
* `-a` → show hidden files

**Use Case:**
Check if `inventory.ini` or `playbook.yml` exists.

---

## 3️⃣ `cd`

**What it does:**
Change directory.

```bash
cd foldername
cd ..
cd ~
```

* `..` → one step back
* `~` → home directory

**Use Case:**
Move into your ansible project folder.

---

## 4️⃣ `mkdir`

**What it does:**
Create new folder.

```bash
mkdir ansible-project
```

**Use Case:**
Create folder to store automation files.

---

## 5️⃣ `touch`

**What it does:**
Create empty file.

```bash
touch inventory.ini
touch playbook.yml
```

**Use Case:**
Create Ansible inventory and playbook file.

---

## 6️⃣ `rm`

**What it does:**
Delete file.

```bash
rm file.txt
rm -r foldername
```

⚠ Be careful. No recycle bin.

---

# 🔹 PART 2 — File Viewing (Very Important)

---

## 7️⃣ `cat`

**What it does:**
Show file content.

```bash
cat inventory.ini
```

**Use Case:**
Quickly check inventory content.

---

## 8️⃣ `nano`

**What it does:**
Open file editor.

```bash
nano inventory.ini
```

**Use Case:**
Edit Ansible inventory or playbook.

---

## 9️⃣ `less`

**What it does:**
View large file page by page.

```bash
less /var/log/syslog
```

**Use Case:**
Check logs when automation fails.

---

# 🔹 PART 3 — System & User Checks

---

## 🔟 `whoami`

**What it does:**
Shows current user.

```bash
whoami
```

**Purpose:**
Check if you are root or normal user.

---

## 1️⃣1️⃣ `sudo`

**What it does:**
Run command as administrator.

```bash
sudo apt update
```

**Use Case:**
Install Ansible, install tools.

---

## 1️⃣2️⃣ `chmod`

**What it does:**
Change file permission.

```bash
chmod 600 id_rsa
chmod +x script.sh
```

**VERY IMPORTANT for SSH keys**

If permission wrong → SSH will fail.

---

# 🔹 PART 4 — Networking Commands (Must Know 🚀)

---

## 1️⃣3️⃣ `ip addr`

**What it does:**
Show IP address.

```bash
ip addr
```

**Use Case:**
Check your server IP before SSH.

---

## 1️⃣4️⃣ `ip route`

**What it does:**
Show routing table.

```bash
ip route
```

**Use Case:**
Check default gateway.

---

## 1️⃣5️⃣ `ping`

**What it does:**
Test connectivity.

```bash
ping 8.8.8.8
ping google.com
```

**Use Case:**
Check if device reachable before running automation.

---

## 1️⃣6️⃣ `ss -tulnp`

**What it does:**
Show open ports.

```bash
ss -tulnp
```

**Use Case:**
Check if SSH port 22 is open.

---

## 1️⃣7️⃣ `curl`

**What it does:**
Test HTTP/API.

```bash
curl http://example.com
```

**Use Case:**
Test REST API from automation script.

---

# 🔹 PART 5 — SSH (VERY IMPORTANT FOR ANSIBLE)

---

## 1️⃣8️⃣ `ssh`

**What it does:**
Connect to remote server.

```bash
ssh user@192.168.1.10
```

**Use Case:**
Manual login test before Ansible.

---

# 🔹 PART 6 — Install Ansible

First update system:

```bash
sudo apt update
```

Then install:

```bash
sudo apt install ansible -y
```

Check version:

```bash
ansible --version
```

---

# 🔹 PART 7 — Generate SSH Key (Step-by-Step)

This is required for passwordless login.

---

## Step 1: Generate key

```bash
ssh-keygen -t rsa -b 4096
```

Press Enter 3 times.

It will create:

```
~/.ssh/id_rsa
~/.ssh/id_rsa.pub
```

---

## Step 2: Copy key to remote server

```bash
ssh-copy-id user@192.168.1.10
```

Enter password once.

Now passwordless login enabled.

Test:

```bash
ssh user@192.168.1.10
```

If no password asked → Success ✅

---

# 🔹 PART 8 — Create Simple Ansible Inventory

Go to your project folder:

```bash
mkdir ansible-project
cd ansible-project
```

Create inventory:

```bash
nano inventory.ini
```

Add this:

```
[servers]
192.168.1.10
```

Save & exit.

---

# 🔹 PART 9 — Run Ansible Ping

Test connectivity:

```bash
ansible all -i inventory.ini -m ping
```

If everything correct, output:

```
192.168.1.10 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

That means:

✅ SSH working
✅ Python installed on remote
✅ Ansible working

---

# 🎯 What You Must Practice Now

1. Check your IP → `ip addr`
2. Test ping to remote
3. Generate SSH key
4. Copy SSH key
5. Install Ansible
6. Run ansible ping

---
Tell me which one you want 🚀


```
