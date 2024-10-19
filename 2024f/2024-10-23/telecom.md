---
title: "Technical Evolution of Networking"
---

## How to compile
```
pandoc --standalone -t revealjs -o telecom.html telecom.md --slide-level=2 --include-in-header=slides.html
```

Thanks to Sam for the template

## Why Care?
::: {.incremental}
- Engineers and computer scientists are liable to "**reinvent the wheel**." Learning how the wheel was invented can help avoid this problem.
- Engineers and computer scientists may **inherit assumptions** that may no longer be reasonable. Articulating those assumptions can help avoid this problem.
:::

## Objective
- Understand the emergence of the modern packet-switched connectionless network historically.

## Was the Internet an Invention?
> "I don't think it was an invention... It was a collection of ideas that were around at the time. The computer people had always had blocks, and lines were always around; that was nothing new ... the real issue was to carry through and see that it was important and it was economic and it was going to have an influence and make sure it happened."
>
> Larry Roberts, ARPANET Program Manager (Pelkey, 1988) 

# Human-Computer Dynamics

## Human-in-the-loop?

This used to be literal.
![Betty Jennings and Fran Bilas operating the ENIAC](images/ENIAC.jpg){width="80%"}

## Development in Electronics

- As microelectronics became **cheaper and more reliable**, a distinction emerged:
  - **I/O**: slow, complex, prone to mechanical failure
  - **Mainframe**: fast, simple, less prone to mechanical failure

## Strachey's Time-Sharing

- In 1959, "time-sharing" emerged—arguably from multiple sources (McCarthy, 1983). 
- In today's language, we may refer to it more like **interrupt-based multiprocessing**. 
  - Slow I/O could **interrupt** the mainframe whenever it was done with its task.

## Strachey on "Interactivity"

- It's still batch processing, focused on debugging batch calculations.

> "There will be three operator's consoles: an engineer's console for maintaining and testing the machine, a programme-testing console with various visual displays and at least an electric typewriter, and a main operator's console. All three will have fairly extensive facilities for intervening in the course of a calculation."
>
> Christopher Strachey (Strachey, 1959)

::: {.notes}
- Strachey's time-sharing (Strachey, 1959) was more like concurrent batch processing. In his time, I/O devices would perform complex (expensive!) operations to read and write data from magnetic tape while the main computer had to wait. Now "interrupts" entered the lexicon, which caught on. As the cost of computing was driven down by the development of electronics, devices could be categorized as slow or fast; simple or complex.
    - "There will be three operator's consoles: an engineer's console for maintaining and testing the machine, a programme-testing console with various visual displays and at least an electric typewriter, and a main operator's console. All three will have fairly extensive facilities for intervening in the course of a calculation." - Christopher Strachey, "Time Sharing in Large Fast Computers"
    - "Who invented interrupts anyway? I thought of them, but I don't believe I mentioned the idea to anyone before I heard of them from other sources." - John McCarthy, Reminisces on the Theory of Time-Sharing
:::

## Changes in Interactivity

- In 1962, just a few years after Strachey, time-sharing started to be about interactivity, a new principle concurrent with time-sharing. Again, the focus was on debugging.

## Debugging

> "Using current batch monitor techniques, as is done on most large computers, each program bug usually requires several hours to eliminate, if not a complete day. The only alternative presently available is for the programmer to attempt to debug directly at the computer, a process which is grossly wasteful of computer time and hampered seriously by the poor console communication usually available. Even if a typewriter is the console, there are usually lacking the sophisticated query and response programs which are vitally necessary to allow effective interaction."
>
> Corbató et al. (Corbató et al., 1962)


## Talking to Your Computer

- In the 1960s, human computer interaction shifted from "operating a machine" to "having a phone call".

> "The effect of this time-sharing is to allow a **conversation** between the user and the computer, at speeds suitable to the user, and this proves to be one of the most significant features, giving the system great versatility. One effect of this conversational mode of operation is that most interactions involve very small amounts of computer time."
>
> Donald Davies (Davies, 1966) (emphasis mine)

# Military Concerns

## Could the 1960s telephone network survive a nuclear attack?

- No, said Paul Baran of the RAND corporation. 

## How does one create a resilient network?

> "We will soon be living in an era in which we cannot guarantee survivability of any single point. However, we can still design systems in which system destruction requires the enemy to pay the price of destroying n of n stations."
>
> Paul Baran (Baran, 1962)

::: {.notes}
- Interesting sidenote: Baran conceived of an "adversarial model" of error in this paper, where everyday reliability errors are imagined to be created by an intentional adversary.
:::

## Implications of Redundancy
- To Baran, packet switching seemed like a natural outgrowth of a distributed, redundant network. 

> "Therefore, we would like to consider the interconnection, one day, of many **all-digital** links to provide a resource optimized for the handling of data for many potential intermittent users..."
>
> Paul Baran (Baran, 1964)

# Combining the Two

## Networks Before ARPA
- Devices were connected before ARPA (e.g. CTSS) but these were primarily TTYs (actual electro-mechanical typewriters, not video display terminals) connected to a mainframe.
- Remote connections between devices could happen over a "wide-area network." Users could type messages onto a strip of tape, and send it encoded into Baudot code into receiver at the mainframe.

## What is Unique About ARPANET?
- Host-to-Host
- Packet Switched
- Inter-"networked"

<!-- CUT FOR HISTORY -->
<!--
## ARPA's Start
- The Advanced Research Projects Agency's (ARPA) Information Processing Techniques Office (IPTO) wanted to connect universities supported by its funding. 
- Larry Roberts deployed a 1200 bps phone line to connect two areas of Lincoln Labs, and everything worked well enough—except for the network itself, which was slow and unreliable. Getting around that constraint signified the main thrust of the ARPANET project.

## BBN's Start

- In order to deploy a capable network, ARPA contracted Bolt, Beranek, and Newman (BBN) for the job.
- To this end they develoeped the IMP, a ruggedized Honeywell mini-computer with telephone modems attached.
-->

# Early ARPANET

## Architecting the ARPANET
- Architectural paradigms in the 60s-70s were dominated by the **Master/Slave** OS paradigm.

> "You try to connect two such devices together, two computers together, and they only know how to talk to each other as if one is the master. Well, if one is the master, then the other must be the slave. We knew that we wanted a much more flexible vision in which the initiative could be at either site, and there would be a coordinated or cooperative model of communications."
>
> John Crocker @ BBN (Pelkey, 2014, Section 6.5)

## Host-Host and NCP
- In order to develop this vision, new protocols had to be developed
  - Network Control Protocol (NCP)
  - Host-Host Protocol

## RFC 33
> After a sending HOST has sent a message to a receiving HOST over a particular link, the sending HOST is prohibited from sending another message over that same link until the sending HOST receives a RFMN.  The RFNM is generated by the IMP connected to the receiving HOST, and the RFNM is sent back to the sending HOST after the message has entered the receiving HOST.  It is important to remember that there are 356 links in each direction and that **no relationship among these is imposed by the network.**
>
> (emphasis mine)

## "Packet-Switched"
- ARPANET was formally packet-switched, but did not support the conventions we tend to associated with packet-switched networks. It established reliable physical circuits that would acknowledge each message over an unreliable network. 

> "... at each node, a copy of the message is stored until it is safely received at the following node." 
>
> Frank E. Heart (Heart et al., 1969)

## Kleinrock on Working with BBN
> "In the early days, when they came out with their proposal, we looked in their routing algorithm, which we were very interested in, and said: 'This thing has loops. A packet can go back and forth, or in a circle.' And they said: 'No, there are no loops.' But there are loops! They said: 'No.' So we simulated them and said: 'Look, there's loops.' They said: 'There are no loops.' Then this four node network was implemented and we showed them loops, and the answer was; 'Yes, there are loops.'"
>
> Len Kleinrock @ UCLA (Pelkey, 2014, Section 6.7)

## ARPANET into TCP/IP
- Many lay-histories of the internet give complete continuity between ARPANET and TCP/IP, neglecting that many ARPANET designers moved towards X.25.
- This can also ignore how the needs of computer users fundamentally changed.

# Transformations of the 70s

## New Computing
- Video display terminals became more common, giving end-users more powerful tools to interact with their computers.
- Minicomputers became financially reasonable for small companies, with personal computers on the way.

## New Networking
- Small institutions were now interested in buying their own mini-computer and setting up their own network.
- Computing now made sense for most institutions.

## Inter-Networking

- The INWG: IFIP Working Group 6.1 (WG 6.1) on Network Interconnection was formed to manage the concept of these inter-networks.
- Notable players were 3 protocol "families":
  - X.25
  - CYCLADES
  - TCP

## X.25

- The standard proposed by international postal, telegraph, and telephone services (PTT).
- Developed to use connection-oriented virtual circuits.
- Provided its own reliability guarantees through LAPB, its link-layer protocol. 

## CYCLADES

- CYCLADES, headed by Louis Pouzin, tried to finish what appeared lacking in ARPANET.

> "[BBN] understood that I intended to build another network but they really didn't believe it. They had this feeling that the ARPANET, this kind of complicated system, could only be implemented in a country like the States due to money, expertise and so on. They didn't believe Europe could bring something like that up."
>
> Louis Pouzin (Pelkey, 2014, Section 8.3)

## TCP/IP

- Through its conflict with CYCLADES, TCP refined itself into TCP/IP, a layered, best-effort, end-to-end set of protocols designed to promote internetworking.

# "Principles" of TCP/IP
- Datagrams
- Layering
- End-to-End Design
- Best-Effort

## What ties these together?
- Minimizing the importance of the network.
- Bringing functionality to the network meant dealing with the postal, telegraph, and telephone services, which were a thorn in the side of the inter-networking standards group.

## Cerf on Datagrams

> "[PTT and INWG] used to fight tooth and nail with each other, and I was out there fighting too. I was beating the table saying: 'God damn it, it had to be datagrams because that required less of a network and you had to do things end-to-end anyway, because you wanted to have the mainframes assure the other end that they had really gotten the data, and not just that the network thinks that you got it..."
>
> Vint Cerf (Pelkey, 2014, Section 8.4)

## Pouzin on Layering

> "The second thing is [TCP version 1] mingled – it actually handled in the very same protocol, matters that belong to the transport level, and matters that belong to the end-to-end protocol. That kind of coupling was politically unacceptable, because these two levels of system were handled by two different worlds: The PTTs and the other world, the computer people. So obviously it was not acceptable in terms of technical sociology. You could not sell something that involves the consensus of these two different worlds."
>
> Louis Pouzin (Pelkey, 2014, Section 8.4)

## Pouzin on End-to-End Design

- Pouzin was open to non-end-to-end solutions to problems, provided that the solutions were emergent and not dictated by the PTT.

> "With experience gradually building up, and depending on trends in international standards, more stable characteristics will eventually emerge. By putting them at some lower system level, it will be possible to obtain higher efficiency and reduce duplication, at the cost of freezing a few more parameters."
>
> Louis Pouzin (Pouzin, 1973)

## What do these Mean Now?
- In the era of microservices, computing clusters, and smart fridges replicating the internet on one device, should we reconsider these assumptions?

# Sources 
<div class="scrollable">
- [Paul Baran - On Distributed Communications Networks - 1962](https://www.rand.org/content/dam/rand/pubs/papers/2005/P2626.pdf)
- [Paul Baran - On Distributed Communications - 1964](https://www.rand.org/pubs/research_memoranda/RM3420.html)
- [Fernando Corbato et al. - An Experimental Time-Sharing System - 1962](http://larch-www.lcs.mit.edu:8001/~corbato/sjcc62/)
- [Donald Davies - Proposal for a Digital Communication Network - 1966](https://www.dcs.gla.ac.uk/~wpc/grcs/Davies05.pdf)
- [Frank Heart et al. - The Interface Message Processor for the ARPA Computer Network - 1969](https://www.walden-family.com/public/1970-imp-afips.pdf)
- [John McCarthy - Reminiscences on the Theory of Time-Sharing - 1983](http://jmc.stanford.edu/computing-science/timesharing.html)
- [James Pelkey - Entrepreneurial Capitalism and Innovation: A History of Computer Communications 1968-1988 - 2014](https://historyofcomputercommunications.info/)
- [Christopher Strachey - Time Sharing in Large Fast Computers - 1959](https://ia804601.us.archive.org/0/items/large-fast-computers/Image070917171847.pdf)
- [Larry Roberts - Interview by James L. Pelkey - 1988](http://archive.computerhistory.org/resources/access/text/2013/04/102746626-05-01-acc.pdf)
- [Louis Pouzin - Presentation on the Major Design Aspects of the CYCLADES Computer Network - 1973](https://dl.acm.org/doi/pdf/10.1145/800280.811034)
</div>
