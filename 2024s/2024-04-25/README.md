---
title: "Zeroconf"
---

## How to compile

Compile me with:

```
pandoc --standalone --to=revealjs --output=README.html README.md --slide-level=2
```

## Objectives

## Preliminaries

- Wide-area network (wan) vs local-area network (LAN)
- Internet Protocol (IP)
  - Connectionless (delivers packets unreliably)
  - IP address (base 10)
  - Internal/external
- Unicast vs broadcast
  - LAN Broadcast address 255.255.255.x

## Traditional networking

- DHCP delivers IP of [some fixed things](https://www.wikiwand.com/en/Dhcp#Options) (including DNS)
- DNS delivers IP of everything else

## Example

- Bob: Hey everone! I'm new here. Can I have 192.168.2.44?
- DHCP server: Bob, yes you may have 192.168.2.44. Here is our networks DNS server 192.168.2.56
- _A few moments later_
- Bob: Hello DNS server (192.168.2.56), who is "printer.local"?
- DNS server: Oh, that's 192.168.2.98

##  Ho to add a new printer?

- Requires server admin
- Server admin: _[Plugs in printer to network]_
- Printer: Hey everyone! I'm new here. Can I have IP ...?
- DHCP server: Printer, yes you may have ...
- Server admin: DHCP server, what address did you give the printer?
- DHCP server: ...
- Server admin: DNS server, please send "printer2.local" to ...

## Zeroconf

- Idea: Use multicast IP address to send DNS request
- Special semantics for *.local
  - "considered a problem by some members of the IETF"
- Protocols: Multicast DNS (MDNS), Micro$oft's Link-Local Multicast Name Resolution
- MDNS Clients: Apple Bonjour, Avahi (open), Systemd

## Example

- Bob: Hey everyone, who has "printer.local"?
- Printer: I do.
- Bob: Ok, noted.
- Alice: I didn't ask, but ok. Also noted.

## DNS Service Discovery (DNS-SD)

- What if we don't know the domain-name of printer?
- Broadcast a DNS request for PTR and TXT records
- [Service types in DNS-SD](http://www.dns-sd.org/ServiceTypes.html)
- Could use WS-Discovery instead of DNS-SD 

---

![](https://upload.wikimedia.org/wikipedia/commons/e/e0/Bonjour_Browser_window.png)

## Clients

- Systemd (lol)
- Others

## Trust issues

- Do you trust the entire network?
- Attacker can learn your devices
- Devices can lie

## Other issues

- Separate broadcast domains?
- Name conflicts

## Related ideas

- Managed vs unmanaged service directory
  - Managed: LDAP, DNS, others
  - Unmanaged: mDNS, Bluetooth SDP
- Service description language
- Service mesh
- Leader election
