```java
 - spine-1:
 
hostname SPINE-1
interface Ethernet2
   no switchport
   ip address 172.16.200.1/30
!
interface Ethernet3
   no switchport
   ip address 172.16.200.5/30
!
interface Ethernet4
   no switchport
   ip address 172.16.200.9/30
!
interface Ethernet5
   no switchport
   ip address 172.16.200.13/30

interface Loopback0
   ip address 172.16.0.1/32
!
ip routing
!
router bgp 65001
   router-id 172.16.0.1
   maximum-paths 2 ecmp 2
   neighbor 172.16.0.3 remote-as 65101
   neighbor 172.16.0.3 update-source Loopback0
   neighbor 172.16.0.3 ebgp-multihop
   neighbor 172.16.0.3 send-community extended
   neighbor 172.16.0.4 remote-as 65101
   neighbor 172.16.0.4 update-source Loopback0
   neighbor 172.16.0.4 ebgp-multihop
   neighbor 172.16.0.4 send-community extended
   neighbor 172.16.0.5 remote-as 65103
   neighbor 172.16.0.5 update-source Loopback0
   neighbor 172.16.0.5 ebgp-multihop
   neighbor 172.16.0.5 send-community extended
   neighbor 172.16.0.6 remote-as 65103
   neighbor 172.16.0.6 update-source Loopback0
   neighbor 172.16.0.6 ebgp-multihop
   neighbor 172.16.0.6 send-community extended
   neighbor 172.16.200.2 remote-as 65101
   neighbor 172.16.200.6 remote-as 65101
   neighbor 172.16.200.10 remote-as 65103
   neighbor 172.16.200.14 remote-as 65103
   !
   address-family evpn
      neighbor 172.16.0.3 activate
      neighbor 172.16.0.4 activate
      neighbor 172.16.0.5 activate
      neighbor 172.16.0.6 activate
   !
   address-family ipv4
      no neighbor 172.16.0.3 activate
      no neighbor 172.16.0.4 activate
      no neighbor 172.16.0.5 activate
      no neighbor 172.16.0.6 activate
      network 172.16.0.1/32



=======================================================
SPINE-2
=======================================================
hostname SPINE-2
interface Ethernet2
   no switchport
   ip address 172.16.200.17/30
!
interface Ethernet3
   no switchport
   ip address 172.16.200.21/30
!
interface Ethernet4
   no switchport
   ip address 172.16.200.25/30
!
interface Ethernet5
   no switchport
   ip address 172.16.200.29/30

   
interface Loopback0
   ip address 172.16.0.2/32
!
ip routing
!
router bgp 65001
   router-id 172.16.0.2
   maximum-paths 2 ecmp 2
   neighbor 172.16.0.3 remote-as 65101
   neighbor 172.16.0.3 update-source Loopback0
   neighbor 172.16.0.3 ebgp-multihop
   neighbor 172.16.0.3 send-community extended
   neighbor 172.16.0.4 remote-as 65101
   neighbor 172.16.0.4 update-source Loopback0
   neighbor 172.16.0.4 ebgp-multihop
   neighbor 172.16.0.4 send-community extended
   neighbor 172.16.0.5 remote-as 65103
   neighbor 172.16.0.5 update-source Loopback0
   neighbor 172.16.0.5 ebgp-multihop
   neighbor 172.16.0.5 send-community extended
   neighbor 172.16.0.6 remote-as 65103
   neighbor 172.16.0.6 update-source Loopback0
   neighbor 172.16.0.6 ebgp-multihop
   neighbor 172.16.0.6 send-community extended
   neighbor 172.16.200.18 remote-as 65101
   neighbor 172.16.200.22 remote-as 65101
   neighbor 172.16.200.26 remote-as 65103
   neighbor 172.16.200.30 remote-as 65103
   !
   address-family evpn
      neighbor 172.16.0.3 activate
      neighbor 172.16.0.4 activate
      neighbor 172.16.0.5 activate
      neighbor 172.16.0.6 activate
   !
   address-family ipv4
      no neighbor 172.16.0.3 activate
      no neighbor 172.16.0.4 activate
      no neighbor 172.16.0.5 activate
      no neighbor 172.16.0.6 activate
      network 172.16.0.2/32

=======================================================
LEAF-1
=======================================================
hostname LEAF-1
interface Ethernet2
   no switchport
   ip address 172.16.200.2/30

interface Ethernet3
   no switchport
   ip address 172.16.200.18/30
   
interface Loopback0
   ip address 172.16.0.3/32
!
interface Loopback1
   ip address 1.1.1.1/32
 ip add 99.99.99.99/32 second
! 
ip routing
!
vlan 2001

interface ethernet 4
  channel-group 10 mode active
  no switchport access vlan 2001
  exi
  
  interface po10
  switchport mode trunk
  mlag 10
  no shutdown


vrf instance vrf1

ip routing vrf vrf1

int vlan2001
vrf vrf1
ip add virtual 172.16.115.1/24
mtu 9000
no autostate

int vlan2002
vrf vrf1
ip add virtual 172.16.118.1/24
mtu 9000
no autostate
!
int lo901
  mtu 9000
   no autostate
   vrf vrf1
ip add 200.200.200.1/32
!
interface Vxlan1
   vxlan source-interface Loopback1
   vxlan udp-port 4789
   vxlan vlan 2001 vni 120010
   vxlan vlan 2002 vni 120020
   vxlan vrf vrf1 vni 1001
!
interface Loopback901
   vrf vrf1
   ip address 200.200.200.1/32

vlan 4094
   name MLAG-BRDR-LEAF
   trunk group MLAG-BRDR-LEAF
!
interface Vlan4094
description MLAG-PEER-LINK
   ip address 169.254.0.1/30
no shutdown

interface Ethernet6
   channel-group 42 mode active
!
interface Ethernet7
   channel-group 42 mode active

interface Ethernet1
   no switchport
   vrf vrf1
   ip address 172.17.200.42/30
   
interface Ethernet5
   no switchport
   vrf vrf1
   ip address 172.17.200.38/30

!
interface Port-Channel42
   switchport trunk allowed vlan 2001,4094
   switchport mode trunk
   switchport trunk group MLAG-BRDR-LEAF
!
mlag configuration
   domain-id MLAG-1
   local-interface Vlan4094
   peer-address 169.254.0.2
   peer-link Port-Channel42

ip virtual-router mac-address 00:1c:73:00:00:01

router bgp 65101
   router-id 172.16.0.3
   maximum-paths 2 ecmp 2
   neighbor 172.16.0.1 remote-as 65001
   neighbor 172.16.0.1 update-source Loopback0
   neighbor 172.16.0.1 ebgp-multihop
   neighbor 172.16.0.1 send-community extended
   neighbor 172.16.0.2 remote-as 65001
   neighbor 172.16.0.2 update-source Loopback0
   neighbor 172.16.0.2 ebgp-multihop
   neighbor 172.16.0.2 send-community extended
   neighbor 172.16.200.1 remote-as 65001
   neighbor 172.16.200.17 remote-as 65001
   !
   address-family evpn
      neighbor 172.16.0.1 activate
      neighbor 172.16.0.2 activate
   !
   address-family ipv4
      no neighbor 172.16.0.1 activate
      no neighbor 172.16.0.2 activate
      network 1.1.1.1/32
      network 99.99.99.99/32
      network 172.16.0.3/32
   !
   vrf vrf1
      rd 1.1.1.1:1001
      route-target import evpn 1001:1001
      route-target export evpn 1001:1001
      neighbor 172.17.200.37 remote-as 65101
      neighbor 172.17.200.41 remote-as 65101
      redistribute connected
      !
      address-family ipv4
         neighbor 172.17.200.37 activate
         neighbor 172.17.200.41 activate



=======================================================
LEAF-2
=======================================================

hostname LEAF-2

vlan 2001

vlan 4094
   name MLAG-BRDR-LEAF
   trunk group MLAG-BRDR-LEAF
!
interface Vlan4094
description MLAG-PEER-LINK
   ip address 169.254.0.2/30
no shutdown

interface Ethernet6
   channel-group 42 mode active
!
interface Ethernet7
   channel-group 42 mode active
!
interface Port-Channel42
   switchport trunk allowed vlan 2001,4094
   switchport mode trunk
   switchport trunk group MLAG-BRDR-LEAF
!
mlag configuration
   domain-id MLAG-1
   local-interface Vlan4094
   peer-address 169.254.0.1
   peer-link Port-Channel42

ip virtual-router mac-address 00:1c:73:00:00:01

interface Ethernet2
   no switchport
   ip address 172.16.200.6/30

interface Ethernet3
   no switchport
   ip address 172.16.200.22/30
   
interface Ethernet5
  no switchport
  vrf vrf1
  ip address 172.17.200.34/30
  no shu
  exit

   
interface Loopback0
   ip address 172.16.0.4/32
!
interface Loopback1
   ip address 1.1.1.1/32
 ip add 99.99.99.99/32 second
! 
ip routing
!
vlan 2001

interface ethernet 4
  channel-group 10 mode active
  no switchport access vlan 2001
  exi
  
  interface po10
  switchport mode trunk
  mlag 10
  no shutdown

vrf instance vrf1

ip routing vrf vrf1

int vlan2001
vrf vrf1
ip add virtual 172.16.115.1/24
!
int lo901
  mtu 9000
   no autostate
   vrf vrf1
ip add 200.200.200.1/32
!
interface Vxlan1
   vxlan source-interface Loopback1
   vxlan udp-port 4789
   vxlan vlan 2001 vni 120010
   vxlan vlan 2002 vni 120020
   vxlan vrf vrf1 vni 1001
!
interface Loopback901
   vrf vrf1
   ip address 200.200.200.1/32

router bgp 65101
   router-id 172.16.0.4
   maximum-paths 2 ecmp 2
   neighbor 172.16.0.1 remote-as 65001
   neighbor 172.16.0.1 update-source Loopback0
   neighbor 172.16.0.1 ebgp-multihop
   neighbor 172.16.0.1 send-community extended
   neighbor 172.16.0.2 remote-as 65001
   neighbor 172.16.0.2 update-source Loopback0
   neighbor 172.16.0.2 ebgp-multihop
   neighbor 172.16.0.2 send-community extended
   neighbor 172.16.200.5 remote-as 65001
   neighbor 172.16.200.21 remote-as 65001
   !
   address-family evpn
      neighbor 172.16.0.1 activate
      neighbor 172.16.0.2 activate
   !
   address-family ipv4
      no neighbor 172.16.0.1 activate
      no neighbor 172.16.0.2 activate
      network 1.1.1.1/32
      network 99.99.99.99/32
      network 172.16.0.4/32
   !
   vrf vrf1
      rd 2.2.2.2:1001
      route-target import evpn 1001:1001
      route-target export evpn 1001:1001
      neighbor 172.17.200.33 remote-as 65101
      neighbor 172.17.200.45 remote-as 65101
      redistribute connected
      !
      address-family ipv4
         neighbor 172.17.200.33 activate
         neighbor 172.17.200.45 activate

=======================================================
RT-WAN-1
=======================================================
hostname RT-WAN-1
!
ip vrf CUSTOMER_01A
 rd 10:2010
 route-target export 10:2010
 route-target import 10:2010
 route-target import 1001:1001
!
ip vrf vrf1
 rd 5.5.5.5:1001
 route-target export 1001:1001
 route-target import 1001:1001
 route-target import 10:2010
!
!
redundancy
!
crypto ikev2 proposal IKE-PROP
 encryption aes-cbc-256
 integrity sha256
 group 14
!
crypto ikev2 policy IKE-POL
 proposal IKE-PROP
!
crypto ikev2 keyring VPN-KEYRING
 peer CUST01
  address 198.51.100.10
  pre-shared-key local cisco123
  pre-shared-key remote cisco123
 !
!
!
crypto ikev2 profile IKEv2_Prof_CUST01
 match identity remote address 198.51.100.10 255.255.255.252
 authentication remote pre-share
 authentication local pre-share
 keyring local VPN-KEYRING
!
!
!
!
!
!
!
!
!
!
!
!
crypto ipsec transform-set VPN-TS esp-aes 256 esp-sha256-hmac
 mode tunnel
!
crypto ipsec profile IPSEC_CUST01
 set transform-set VPN-TS
 set pfs group14
 set ikev2-profile IKEv2_Prof_CUST01
 responder-only
!
!
!
!
!
!
!
!
!
!
interface Loopback0
 description Router-id
 ip address 172.16.0.7 255.255.255.255
!
interface Tunnel0
 description CUST01
 ip vrf forwarding CUSTOMER_01A
 ip address 10.255.100.1 255.255.255.252
 tunnel source 198.51.100.14
 tunnel mode ipsec ipv4
 tunnel destination 198.51.100.10
 tunnel protection ipsec profile IPSEC_CUST01
!
interface GigabitEthernet1
 ip vrf forwarding vrf1
 ip address 172.17.200.41 255.255.255.252
 negotiation auto
 no mop enabled
 no mop sysid
!
interface GigabitEthernet2
 ip vrf forwarding vrf1
 ip address 172.17.200.45 255.255.255.252
 negotiation auto
 no mop enabled
 no mop sysid
!
interface GigabitEthernet3
 description Internet-WAN
 ip address 198.51.100.9 255.255.255.248
 standby 1 ip 198.51.100.14
 standby 1 priority 110
 standby 1 preempt
 negotiation auto
 no mop enabled
 no mop sysid
!
interface GigabitEthernet4
 no ip address
 negotiation auto
 no mop enabled
 no mop sysid
!
interface GigabitEthernet4.101
 description CUST01_VIA_WAN-SW-1
 encapsulation dot1Q 101
 ip vrf forwarding CUSTOMER_01A
 ip address 172.17.101.1 255.255.255.252
!
!
router bgp 65101
 bgp log-neighbor-changes
 !
 address-family ipv4
  network 172.16.0.7 mask 255.255.255.255
 exit-address-family
 !
 address-family ipv4 vrf CUSTOMER_01A
  redistribute connected
  neighbor 10.255.100.2 remote-as 1234
  neighbor 10.255.100.2 activate
  neighbor 172.17.101.2 remote-as 1234
  neighbor 172.17.101.2 activate
 exit-address-family
 !
 address-family ipv4 vrf vrf1
  redistribute static
  neighbor 172.17.200.42 remote-as 65101
  neighbor 172.17.200.42 activate
  neighbor 172.17.200.46 remote-as 65101
  neighbor 172.17.200.46 activate
 exit-address-family
!
ip forward-protocol nd
ip http server
ip http authentication local
ip http secure-server



=======================================================
RT-WAN-2
=======================================================
conf t
hostname RT-WAN-2
!
ip vrf CUSTOMER_01A
 rd 10:2010
 route-target export 10:2010
 route-target import 10:2010
 route-target import 1001:1001
exit
ip vrf vrf1
 rd 6.6.6.6:1001
 route-target export 1001:1001
 route-target import 1001:1001
 route-target import 10:2010
exit
crypto ikev2 proposal IKE-PROP
 encryption aes-cbc-256
 integrity sha256
 group 14
exit
crypto ikev2 policy IKE-POL
 proposal IKE-PROP
exit
crypto ikev2 keyring VPN-KEYRING
 peer CUST01
  address 198.51.100.10
  pre-shared-key local cisco123
  pre-shared-key remote cisco123
exit
exit
crypto ikev2 profile IKEv2_Prof_CUST01
 match identity remote address 198.51.100.10 255.255.255.252
 authentication remote pre-share
 authentication local pre-share
 keyring local VPN-KEYRING
exit
crypto ipsec transform-set VPN-TS esp-aes 256 esp-sha256-hmac
 mode tunnel
exit
crypto ipsec profile IPSEC_CUST01
 set transform-set VPN-TS
 set pfs group14
 set ikev2-profile IKEv2_Prof_CUST01
exit
interface Loopback0
 description Router-id
 ip address 172.16.0.8 255.255.255.255
exit
interface Tunnel0
 description CUST01
 ip vrf forwarding CUSTOMER_01A
 ip address 10.255.100.1 255.255.255.252
 tunnel source 198.51.100.14
 tunnel mode ipsec ipv4
 tunnel destination 198.51.100.10
 tunnel protection ipsec profile IPSEC_CUST01 
exit

interface GigabitEthernet3
 description Internet-WAN
 ip address 198.51.100.11 255.255.255.248
 standby 1 ip 198.51.100.14
 standby 1 priority 100
 standby 1 preempt
 negotiation auto
exit

interface GigabitEthernet1
 ip vrf forwarding vrf1
 ip address 172.17.200.37 255.255.255.252
 negotiation auto
 no mop enabled
 no mop sysid
!
interface GigabitEthernet2
 ip vrf forwarding vrf1
 ip address 172.17.200.33 255.255.255.252
 negotiation auto
 no mop enabled
 no mop sysid
!
interface GigabitEthernet4
 no ip address
 negotiation auto
 no mop enabled
 no mop sysid
!
interface GigabitEthernet4.201
 description CUST01_VIA_WAN-SW-1
 encapsulation dot1Q 101
 ip vrf forwarding CUSTOMER_01A
 ip address 172.17.102.1 255.255.255.252

router bgp 65101
 bgp log-neighbor-changes
 !
 address-family ipv4
  network 172.16.0.8 mask 255.255.255.255
 exit-address-family
 !
 address-family ipv4 vrf CUSTOMER_01A
  redistribute connected
  neighbor 10.255.100.2 remote-as 1234
  neighbor 10.255.100.2 activate
  neighbor 172.17.102.2 remote-as 1234
  neighbor 172.17.102.2 activate
 exit-address-family
 !
 address-family ipv4 vrf vrf1
  redistribute static
  neighbor 172.17.200.34 remote-as 65101
  neighbor 172.17.200.34 activate
  neighbor 172.17.200.38 remote-as 65101
  neighbor 172.17.200.38 activate
 exit-address-family

=======================================================
LEAF-3
=======================================================
hostname LEAF-3

interface Ethernet2
   no switchport
   ip address 172.16.200.10/30

interface Ethernet3
   no switchport
   ip address 172.16.200.26/30
   
interface Loopback0
   ip address 172.16.0.5/32
!
interface Loopback1
   ip address 3.3.3.3/32
 ip add 99.99.99.99/32 second
 
 interface Loopback901
   vrf vrf1
   ip address 200.200.200.2/32
! 
ip routing
!
vlan 2003

interface po10
 switchport mode trunk
  mlag 10
  no shutdown
  
  interface ethernet 4
  no switchport access vlan 2003
  channel-group 10 mode active
  exi
  
  interface ethernet 1
  channel-group 10 mode active
  exit

vrf instance vrf1

ip routing vrf vrf1

int vlan2003
vrf vrf1
ip add virtual 172.16.116.1/24
!
int lo901
  mtu 9000
   no autostate
   vrf vrf1
ip add 200.200.200.1/32
!
interface Vxlan1
   vxlan source-interface Loopback1
   vxlan udp-port 4789
   vxlan vlan 2003 vni 120030
   vxlan vrf vrf1 vni 1001
!
vlan 4094
   name MLAG-BRDR-LEAF
   trunk group MLAG-BRDR-LEAF
!
interface Vlan4094
description MLAG-PEER-LINK
   ip address 169.254.1.1/30
no shutdown

interface Ethernet6
   channel-group 42 mode active
!
interface Ethernet7
   channel-group 42 mode active
!
interface Port-Channel42
   switchport trunk allowed vlan 2003,4094
   switchport mode trunk
   switchport trunk group MLAG-BRDR-LEAF
!
mlag configuration
   domain-id MLAG-1
   local-interface Vlan4094
   peer-address 169.254.1.2
   peer-link Port-Channel42

ip virtual-router mac-address 00:1c:73:00:00:02

router bgp 65103
   router-id 172.16.0.5
   maximum-paths 2 ecmp 2
   neighbor 172.16.0.1 remote-as 65001
   neighbor 172.16.0.1 update-source Loopback0
   neighbor 172.16.0.1 ebgp-multihop
   neighbor 172.16.0.1 send-community extended
   neighbor 172.16.0.2 remote-as 65001
   neighbor 172.16.0.2 update-source Loopback0
   neighbor 172.16.0.2 ebgp-multihop
   neighbor 172.16.0.2 send-community extended
   neighbor 172.16.200.9 remote-as 65001
   neighbor 172.16.200.25 remote-as 65001
   !
   address-family evpn
      neighbor 172.16.0.1 activate
      neighbor 172.16.0.2 activate
   !
   address-family ipv4
      no neighbor 172.16.0.1 activate
      no neighbor 172.16.0.2 activate
      network 3.3.3.3/32
      network 99.99.99.99/32
      network 172.16.0.5/32
   !
   vrf vrf1
      rd 3.3.3.3:1001
      route-target import evpn 1001:1001
      route-target export evpn 1001:1001
      redistribute connected
	  

=======================================================
LEAF-4
=======================================================
hostname LEAF-4

interface Ethernet2
   no switchport
   ip address 172.16.200.14/30

interface Ethernet3
   no switchport
   ip address 172.16.200.30/30
   
interface Loopback0
   ip address 172.16.0.6/32
!
interface Loopback1
   ip address 3.3.3.3/32
 ip add 99.99.99.99/32 second
 
 interface Loopback901
   vrf vrf1
   ip address 200.200.200.2/32
! 
ip routing
!
vlan 2003

interface po10
 switchport mode trunk
  mlag 10
  no shutdown
  
  interface ethernet 4
  no switchport access vlan 2003
  channel-group 10 mode active
  exi
  
  interface ethernet 1
  channel-group 10 mode active
  exit

vrf instance vrf1

ip routing vrf vrf1

int vlan2003
vrf vrf1
ip add virtual 172.16.116.1/24
!
int lo901
  mtu 9000
   no autostate
   vrf vrf1
ip add 200.200.200.1/32
!
interface Vxlan1
   vxlan source-interface Loopback1
   vxlan udp-port 4789
   vxlan vlan 2003 vni 120030
   vxlan vrf vrf1 vni 1001
!
vlan 4094
   name MLAG-BRDR-LEAF
   trunk group MLAG-BRDR-LEAF
!
interface Vlan4094
description MLAG-PEER-LINK
   ip address 169.254.1.2/30
no shutdown

interface Ethernet6
   channel-group 42 mode active
!
interface Ethernet7
   channel-group 42 mode active
!
interface Port-Channel42
   switchport trunk allowed vlan 2003,4094
   switchport mode trunk
   switchport trunk group MLAG-BRDR-LEAF
!
mlag configuration
   domain-id MLAG-1
   local-interface Vlan4094
   peer-address 169.254.1.1
   peer-link Port-Channel42

ip virtual-router mac-address 00:1c:73:00:00:02

router bgp 65103
   router-id 172.16.0.6
   maximum-paths 2 ecmp 2
   neighbor 172.16.0.1 remote-as 65001
   neighbor 172.16.0.1 update-source Loopback0
   neighbor 172.16.0.1 ebgp-multihop
   neighbor 172.16.0.1 send-community extended
   neighbor 172.16.0.2 remote-as 65001
   neighbor 172.16.0.2 update-source Loopback0
   neighbor 172.16.0.2 ebgp-multihop
   neighbor 172.16.0.2 send-community extended
   neighbor 172.16.200.13 remote-as 65001
   neighbor 172.16.200.29 remote-as 65001
   !
   address-family evpn
      neighbor 172.16.0.1 activate
      neighbor 172.16.0.2 activate
   !
   address-family ipv4
      no neighbor 172.16.0.1 activate
      no neighbor 172.16.0.2 activate
      network 3.3.3.3/32
      network 99.99.99.99/32
      network 172.16.0.6/32
   !
   vrf vrf1
      rd 3.3.3.3:1001
      route-target import evpn 1001:1001
      route-target export evpn 1001:1001
      redistribute connected
	  

=======================================================
HANA
=======================================================
hostname HANA
ip routing
!
ip route 0.0.0.0/0 172.16.115.1

vlan 2001
   name HANA-SERVER
!
vlan 2002

  interface Ethernet4
  switchport access vlan 2002
  exit

interface Port-Channel10
!
interface Port-Channel20
   switchport mode trunk
!
interface Ethernet1
   channel-group 20 mode active
!
interface Ethernet2
   channel-group 20 mode active
!
interface Ethernet3
   switchport access vlan 2001

=======================================================
STR
=======================================================
hostname STR
ip routing

vlan 2001-2004
!
interface Port-Channel20
   switchport mode trunk
!
interface Ethernet1
   channel-group 20 mode active
!
interface Ethernet2
   channel-group 20 mode active
!
interface Ethernet3
   switchport access vlan 2003
!
interface Ethernet4
   switchport access vlan 2004
!
interface Ethernet5
   switchport access vlan 2001
!
interface Ethernet6
   switchport access vlan 2002
!
interface Ethernet7
   switchport access vlan 2003
!
interface Ethernet8
   switchport access vlan 2004

=======================================================
Virtual PC in EVE_NG 
=======================================================

HANA eth3 is connected to EVE-NG Virtual PC15 ( member of Vlan 2001) =172.16.115.100= GW 172.16.115.1
STR eth3 is connected to EVE-NG Virtual PC14 ( member of Vlan 2003) =172.16.116.100= GW 172.16.116.1
STR eth4 is connected to EVE-NG Virtual PC14 ( member of Vlan 2004) =172.16.117.100= GW 172.16.117.1
VPCS> ping 172.16.117.100

172.16.117.100 icmp_seq=1 ttl=64 time=0.001 ms
172.16.117.100 icmp_seq=2 ttl=64 time=0.001 ms
172.16.117.100 icmp_seq=3 ttl=64 time=0.001 ms
172.16.117.100 icmp_seq=4 ttl=64 time=0.001 ms
172.16.117.100 icmp_seq=5 ttl=64 time=0.001 ms

VPCS> ping 172.16.116.100

84 bytes from 172.16.116.100 icmp_seq=1 ttl=63 time=10.050 ms
84 bytes from 172.16.116.100 icmp_seq=2 ttl=63 time=3.956 ms
84 bytes from 172.16.116.100 icmp_seq=3 ttl=63 time=17.882 ms
84 bytes from 172.16.116.100 icmp_seq=4 ttl=63 time=3.543 ms
84 bytes from 172.16.116.100 icmp_seq=5 ttl=63 time=4.361 ms

VPCS> ping 172.16.115.100

84 bytes from 172.16.115.100 icmp_seq=1 ttl=62 time=25.757 ms
84 bytes from 172.16.115.100 icmp_seq=2 ttl=62 time=7.424 ms
84 bytes from 172.16.115.100 icmp_seq=3 ttl=62 time=8.864 ms
84 bytes from 172.16.115.100 icmp_seq=4 ttl=62 time=8.165 ms
84 bytes from 172.16.115.100 icmp_seq=5 ttl=62 time=7.870 ms


=======================================================
CUST-VPN
=======================================================

hostname CUST-VPN
!
!
redundancy
!
crypto ikev2 proposal IKE-PROP
 encryption aes-cbc-256
 integrity sha256
 group 14
!
crypto ikev2 policy IKE-POL
 proposal IKE-PROP
!
crypto ikev2 keyring VPN-KEYRING
 peer CPG
  address 198.51.100.14
  pre-shared-key local cisco123
  pre-shared-key remote cisco123
 !
!
crypto ikev2 profile IKEv2_Prof_CPG
 match identity remote address 198.51.100.14 255.255.255.248
 authentication remote pre-share
 authentication local pre-share
 keyring local VPN-KEYRING
!
!

!
crypto ipsec transform-set VPN-TS esp-aes 256 esp-sha256-hmac
 mode tunnel
!
crypto ipsec profile IPSEC_CPG
 set transform-set VPN-TS
 set pfs group14
 set ikev2-profile IKEv2_Prof_CPG
!
!
!
interface Loopback0
 description Router-id
 ip address 172.72.72.72 255.255.255.255
!
interface Tunnel0
 description CPG
 ip address 10.255.100.2 255.255.255.252
 tunnel source 198.51.100.10
 tunnel mode ipsec ipv4
 tunnel destination 198.51.100.14
 tunnel protection ipsec profile IPSEC_CPG
!
interface GigabitEthernet1
 ip address 192.168.10.100 255.255.255.0
 negotiation auto
 no mop enabled
 no mop sysid
!
interface GigabitEthernet2
 ip address 192.168.20.100 255.255.255.0
 shutdown
 negotiation auto
 no mop enabled
 no mop sysid
!
interface GigabitEthernet3
 ip address 198.51.100.10 255.255.255.252
 negotiation auto
 no mop enabled
 no mop sysid

!
router bgp 1234
 bgp log-neighbor-changes
 neighbor 10.255.100.1 remote-as 65101
 !
 address-family ipv4
  network 192.168.10.0
  network 192.168.20.0
  neighbor 10.255.100.1 activate
 exit-address-family
!
ip forward-protocol nd
ip http server
ip http authentication local
ip http secure-server
ip route 0.0.0.0 0.0.0.0 198.51.100.9
ip route 172.16.115.0 255.255.255.0 Tunnel0
ip route 172.16.116.0 255.255.255.0 Tunnel0
ip route 172.16.117.0 255.255.255.0 Tunnel0
!

!
control-plane

line con 0
 stopbits 1
line vty 0 4
 login
!



```