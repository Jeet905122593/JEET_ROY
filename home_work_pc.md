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
inventory==> device.yaml
scripts ==> ping_test.py

From vscode terminal:

PS C:\Users\JEET_NILADRI\Documents\GitHub\JEET_ROY> dir


    Directory: C:\Users\JEET_NILADRI\Documents\GitHub\JEET_ROY


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2/23/2026  12:28 AM                inventory
d-----         2/23/2026  12:07 AM                scripts
-a----         2/23/2026  12:03 AM          35817 Cisco-vrf-aware-ipsec-vpn.md
-a----         2/23/2026  12:03 AM          18897 Cloud Peering_TEST_JEET.md
-a----         2/18/2026  10:11 PM            625 Data Traffic Flow via Squid Proxy _ HEC2.0.md
-a----         2/18/2026  10:11 PM          33159 hcsm-useful-comments.md
-a----         2/18/2026  10:11 PM          10557 hec01-rdk-outbound.md
-a----         2/23/2026  12:22 AM          25540 runbook.md
-a----         2/18/2026  10:11 PM          15899 vpn-traffic-flow.md


PS C:\Users\JEET_NILADRI\Documents\GitHub\JEET_ROY> dir inventory


    Directory: C:\Users\JEET_NILADRI\Documents\GitHub\JEET_ROY\inventory


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2/23/2026  12:18 AM                sap_proj
-a----         2/23/2026  12:28 AM            283 devices.yaml


PS C:\Users\JEET_NILADRI\Documents\GitHub\JEET_ROY> dir scripts


    Directory: C:\Users\JEET_NILADRI\Documents\GitHub\JEET_ROY\scripts


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         2/23/2026  12:07 AM           1773 ping_test1.py


PS C:\Users\JEET_NILADRI\Documents\GitHub\JEET_ROY>

```