# mDNS notes

- https://en.wikipedia.org/wiki/Multicast_DNS
- https://justanapplication.wordpress.com/category/dns/dns-resource-records/dns-ptr-record/
- https://markhaa.se/posts/multicast-dns-for-pen-testers/#enumeration

# Definitions
- Zeroconf - technologies allowing a network to function without manual configuration (e.g.)
  - includes local network hostname resolution (in lieu of a DHCP server) and service discovery
- mDNS - hostname resolution part of Zeroconf
  - another example of hostname resolution is NetBIOS for Windows
- DNS-SD - service discovery protocol that makes use of standard DNS concepts for advertising services (TXT and SRV records)

# IP Multicast Overview
- like IP broadcast (sending packets to e.g. X.X.X.255) IP multicast allows one device to talk to many
- IP multicast has groups that devices can join.  The router keeps track of which devices have joined which groups
- IP multicast groups are just IP addresses.  When you want to talk to this group, you set the packet destination address to the group
- IP addresses in 224.0.0.1-239.255.255.255 are reserved for multicast

Example multicast groups
- 224.0.0.1   - All
- 224.0.0.251 - mDNS
  
```
# joining a multicast group
sudo ip addr add 239.42.42.42/32 dev enp4s0 autojoin
# listing joined multicast groups
ip maddress show
```

<!-- https://superuser.com/questions/324824/linux-built-in-or-open-source-program-to-join-multicast-group -->

![](broadcast_vs_multicast.jpg)

<!-- https://castr.com/blog/unicast-vs-multicast-vs-broadcast/ -->

# Avahi

- created by Lennart Poettering and others starting in 2005

## advertising services with Avahi



