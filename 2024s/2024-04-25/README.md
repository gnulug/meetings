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

## What is your printer's IP?

- DHCP delivers IP of [some fixed things](https://www.wikiwand.com/en/Dhcp#Options) (including DNS)
- DNS delivers IP of everything else
- How to add a new printer?

## Zeroconf

- IP multicast DNS request
- Special semantics for _foobar_.local
  - "considered a problem by some members of the IETF"
- Bob: Hey everyone, who has "printer.local"?
- Printer: I do.
- Bob: Ok, noted.
- Alice: I didn't ask, but ok. Also noted.
- mDNS, Link-Local Multicast Name Resolution, 

## Clients

- Systemd (lol)
- Others

## Issues

- Separate broadcast domains?
- Lying
- Name conflicts
- Which names are valid?
