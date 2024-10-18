---
title: "Technical Evolution of Networking"
---

## How to compile
```
pandoc --standalone -t revealjs -o telecom.html telecom.md --slide-level=2 -V theme=beige
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

<!-- CUT FOR TIME -->
<!-- 
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
-->

## Talking to Your Computer

- In the 1960s, human computer interaction shifted from factory machine to having a phone call.

> "The effect of this time-sharing is to allow a **conversation** between the user and the computer, at speeds suitable to the user, and this proves to be one of the most significant features, giving the system great versatility. One effect of this conversational mode of operation is that most interactions involve very small amounts of computer time."
>
> Donald Davies (Davies, 1966) (emphasis mine)

# Military Concerns

## Could the 1960s telephone network survive a nuclear detonation?

- No, said Paul Baran of the RAND corporation. 

## How does one create a resilient network?

- Redundancy

> "We will soon be living in an era in which we cannot guarantee survivability of any single point. However, we can still design systems in which system destruction requires the enemy to pay the price of destroying n of n stations."
>
> Paul Baran (Baran, 1962)

::: {.notes}
- Interesting sidenote: Baran conceived of an "adversarial model" of error in this paper, where everyday reliability errors are imagined to be created by an intentional adversary.
:::

## Implications of Redundancy
- To Baran, packet switching seems like a natural outgrowth of a distributed, redundant network. 

> "Therefore, we would like to consider the interconnection, one day, of many **all-digital** links to provide a resource optimized for the handling of data for many potential intermittent users..."
>
> Paul Baran (Baran, 1964)


## Dividing the "End-to-End" from the "Network"
- The main focus was still to establish a physical circuit for these switched networks--the primary advantage was interleaving.
- But if we're being redundant, maybe we can be cheap and unreliable in normal operation.

# Combining the Two

## ARPA's Start

- The Advanced Research Projects Agency's (ARPA) Information Processing Techniques Office (IPTO) wanted to connect universities supported by its funding. 
- Larry Roberts deployed a 1200 bps phone line to connect two areas of Lincoln Labs, and everything worked well enough—except for the network itself, which was slow and unreliable. Getting around that constraint signified the main thrust of the ARPANET project.

## BBN's Start

- In order to deploy a capable network, ARPA contracted Bolt, Beranek, and Newman (BBN) for the job.
- To this end they develoeped the IMP, a ruggedized Honeywell mini-computer with telephone modems attached.

# Early ARPANET

## Architecting the ARPANET
- Architectural paradigms in the 60s-70s were dominated by the "Master/Slave" OS paradigm.

> "You try to connect two such devices together, two computers together, and they only know how to talk to each other as if one is the master. Well, if one is the master, then the other must be the slave. We knew that we wanted a much more flexible vision in which the initiative could be at either site, and there would be a coordinated or cooperative model of communications."
>
> John Crocker @ BBN (Pelkey, 2014, Section 4.5)

## Host-Host and NCP
- In order to develop this vision, new protocols had to be developed
  - Network Control Protocol (NCP)
  - Host-Host Protocol

## RFC 33
> After a sending HOST has sent a message to a receiving HOST over a particular link, the sending HOST is prohibited from sending another message over that same link until the sending HOST receives a RFMN.  The RFNM is generated by the IMP connected to the receiving HOST, and the RFNM is sent back to the sending HOST after the message has entered the receiving HOST.  It is important to remember that there are 356 links in each direction and that **no relationship among these is imposed by the network.**
>
> RFC 33 (emphasis mine)

## "Packet-Switched"
- ARPANET was formally packet-switched, but did not support the conventions we tend to associated with packet-switched networks. It established reliable physical circuits that would acknowledge each message over an unreliable network. 

> "... at each node, a copy of the message is stored until it is safely received at the following node." 
>
> Frank E. Heart (Heart et al., 1969)

## Working Limitations
- Universities could not work with these IMPs freely. It was a network for research, not a researchable network.

## Kleinrock on Working with BBN
> "In the early days, when they came out with their proposal, we looked in their routing algorithm, which we were very interested in, and said: 'This thing has loops. A packet can go back and forth, or in a circle.' And they said: 'No, there are no loops.' But there are loops! They said: 'No.' So we simulated them and said: 'Look, there's loops.' They said: 'There are no loops.' Then this four node network was implemented and we showed them loops, and the answer was; 'Yes, there are loops.'"
>
> Len Kleinrock @ UCLA (Pelkey, 2014, Section 4.7)

## The End of ARPANET

- An incomplete conclusion could be that the ARPANET was doomed to fail.
  - Built off phone lines
  - Designed explicitly for reliable routing
  - Built with non-transparent gateways

## The End of ARPANET?

- However, you could alternatively say that the opposition created between BBN and the academic community, as well as BBN's own confused organization and strained relatioship to ARPA, stunted the possibility of ARPANET's full development.

# ARPANET's Legacy

- Is it true that ARPANET was the direct ancestor of TCP/IP?

## Other influences

- Not directly continuous.

- CYCLADES, a project by the French postal service, headed by Louis Pouzin, tried to finish what appeared lacking in ARPANET
> "[BBN] understood that I intended to build another network but they really didn't believe it. They had this feeling that the Arpanet, this kind of complicated system, could only be implemented in a country like the States due to money, expertise and so on. They didn't believe Europe could bring something like that up."
>
> Louis Pouzin

## Layering in CYCLADES

- CYCLADES was an intervening force for whom we now credit as the inventors of TCP/IP - Cerf, Kahn, and Metcalfe. CYCLADES had explicit layering by modeling to an application an end-to-end virtual circuit on top of an unreliable, best-effort network. With CYCLADES, modern networking concepts become recognizable 
- Later, we would see the protocol wars come out of these delineations.

# "Principles" of the Internet

## End-to-End?
- Why be end-to-end?
    - End-to-end provisioning is useful in that they only need to fix a problem once, at the host, and the host is the device most able to appraise what an error is. Pouzin remained open to alternative solutions: "With experience gradually building up, and depending on trends in international standards, more stable characteristics will eventually emerge. By putting them at some lower system level, it will be possible to obtain higher efficiency and reduce duplication, at the cost of freezing a few more parameters."
    - However, end-to-end solutions are slow, and not every problem that manifests at the host is more easily solved at the host--(e.g. the rapid adoption of ECN).

## Virtual Circuits?
- Why use virtual circuits?
    - To Pouzin, freedom in routing packets.
    - "Although various groups call for a DG [datagram] interface, the carriers are opposed to it. Four carriers are rushing a VC [virtual circuit, to Pouzin this means an exclusively carrier-operated network that requires user subscription to that network] protocol through CCITT [Consultative Committee for International Telephony and Telegraphy, a committee in the International Telegraphers Union]. The carrier's goal is to take over terminal handling, and gradually other processing functions. DG's would leave too much freedom to the customer. The political implications of the carrier policy suggest that better boundaries be drawn up between carriers and data processing."
- However, virtual circuits are hyper-sensitive to network issues--e.g. reorderingas a sign of network congestion

## Layering?
- 
- However, the policy of transparent layering is often violated in a variety of contexts. Quality of Service

## Best-Effort Delivery?
- In the era of microservices, computing clusters, and smart fridges replicating the internet on one host, can we bypass requirements on best-effort delivery?

## Conclusion

- Hopefully, this presentation has illustrated that the development of the (more or less) modern internet was not just a rational adoption of design principles, but rather a process that was marked by nuclear war, academic contention, disorganization, and political visions for an ideal internet.
- Apparent "givens" in design like the end-to-end principle and layering were contingents of a decades-long development in human-computer interaction.

## Discussion
- What assumptions made by early designers ended up violated over time, if any?
- Can the internet realistically be changed? If so, to what extent?

## Sources

- [Paul Baran - On Distributed Communications Networks - 1962](https://www.rand.org/content/dam/rand/pubs/papers/2005/P2626.pdf)
- [Paul Baran - On Distributed Communications - 1964](https://www.rand.org/pubs/research_memoranda/RM3420.html)
- [Richard Bennett - Designed for Change](https://d1bcsfjk95uj19.cloudfront.net/files/2009-designed-for-change.pdf)
- [David Clark - The Design Philosophy of the DARPA Internet Protocols](http://ccr.sigcomm.org/archive/1995/jan95/ccr-9501-clark.pdf)
- [Fernando Corbato et al. - An Experimental Time-Sharing System - 1962](http://larch-www.lcs.mit.edu:8001/~corbato/sjcc62/)
- [Donald Davies - Proposal for a Digital Communication Network - 1966](https://www.dcs.gla.ac.uk/~wpc/grcs/Davies05.pdf)
- [Frank Heart et al. - The Interface Message Processor for the ARPA Computer Network - 1969](https://www.walden-family.com/public/1970-imp-afips.pdf)
- [John McCarthy - Reminiscences on the Theory of Time-Sharing - 1983](http://jmc.stanford.edu/computing-science/timesharing.html)
- [James Pelkey - Entrepreneurial Capitalism and Innovation: A History of Computer Communications 1968-1988 - 2014](https://web.archive.org/web/20210617093154/https://www.historyofcomputercommunications.info/Book/6/6.3-CYCLADESNetworkLouisPouzin1-72.html)
- [Larry Roberts - The ARPANET and Computer Networks](https://dl.acm.org/doi/pdf/10.1145/61975.66916)
- [Christopher Strachey - Time Sharing in Large Fast Computers - 1959](https://ia804601.us.archive.org/0/items/large-fast-computers/Image070917171847.pdf)
- [Larry Roberts - Interview by James L. Pelkey - 1988](http://archive.computerhistory.org/resources/access/text/2013/04/102746626-05-01-acc.pdf)
