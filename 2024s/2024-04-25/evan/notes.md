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

<!-- https://www.iana.org/assignments/multicast-addresses/multicast-addresses.xhtml -->
  
```
# joining a multicast group
sudo ip addr add 239.42.42.42/32 dev enp4s0 autojoin
# listing joined multicast groups
ip maddress show
```

<!-- https://superuser.com/questions/324824/linux-built-in-or-open-source-program-to-join-multicast-group -->

![](broadcast_vs_multicast.jpg)

<!-- https://castr.com/blog/unicast-vs-multicast-vs-broadcast/ -->

IP Multicast Demo

```
# on host
sudo python multicastdemo.py
xterm h1 h2

# in terminal for h1 machine
nc -l -p 1234 -u
# in terminal for h2 machine
nc 224.0.0.100 1234 <<< hello
# nothing happens.  h1 is not part of multicast group

# in terminal for h1 machine
ip addr add 224.0.0.100/32 dev h1-eth0 autojoin
nc -l -p 1234 -u
# in terminal for h2 machine
nc 224.0.0.100 1234 <<< hello
# hello appears on h1 because h1 has joined the .100 multicast group
```

# mDNS overview
- make a DNS request to multicast group 224.0.0.251

```
# on host
systemctl disable avahi-daemon --now
sudo python multicastdemo.py
>>> xterm h1 h2

# in terminal for h2 machine
nc -l -p 5353 -u
# in terminal for h1 machine
avahi-resolve --name foobar.local
# DNS query appears in netcat on h2.  We can manually craft a fixed DNS response
```

# Avahi

- created by Lennart Poettering and others starting in 2005

```
```

## advertising services with Avahi



