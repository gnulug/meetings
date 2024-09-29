---
title: "Technical Evolution of Networking Concepts"
---

## How to compile

DON'T COMPILE ME YET

```
pandoc --standalone --to=revealjs --output=README.html README.md --slide-level=2
```

Thanks to Sam for the template

## Opening Quote

- "I don't think it was an invention; it wasn't a theory breakthrough like Einstein. It was a collection of ideas that were around at the time. The computer people had always had blocks and lines were always around; that was nothing new ... So, those were pieces that we applied, but the real issue was to carry through and see that it was important and it was economic and it was going to have an influence and make sure it happened." - Larry Roberts

## Why care?

- Learn how the wheel was invented.
- Learn how to not take things for granted.

## Objectives

- Cover (in broad strokes) the "whys" behind industry changes and look at "paths not taken"
- A few major transformations in particular:
  - Context - 5 min
  - Evolving into and out of the Telephone Network - 5 min
  - Design Decisions and Outside Influences behind ARPANET - 10 min
  - Discussion Questions - 10 min

## First: Changing Human-Computer Dynamics

## Context

- Strachey's time-sharing (1959) was more like concurrent batch processing--in his time, I/O devices would perform complex (expensive!) operations in order to read and write data from magnetic tape while the main computer had to wait. Now "interrupts" entered the lexicon, which caught on. As the cost of computing was driven down by the development of electronics, devices could be categorized as slow or fast, as simple or complex.
    - "There will be three operator's consoles: an engineer's console for maintaining and testing the machine, a programme-testing console with various visual displays and at least an electric typewriter, and a main operator's console. All three will have fairly extensive facilities for intervening in the course of a calculation." - Christopher Strachey, Time Sharing in Large Fast Computers
    - "Who invented interrupts anyway? I thought of them, but I don't believe I mentioned the idea to anyone before I heard of them from other sources." - John McCarthy, Reminisces on the Theory of Time-Sharing

## Evolving Interactivity

- Only a few years after Strachey, the phrase "time-sharing" changed to talk about interactivity, which was a new principle concurrent with time-sharing.
    - "Using current batch monitor techniques, as is done on most large computers, each program bug usually requires several hours to eliminate, if not a complete day. The only alternative presently available is for the programmer to attempt to debug directly at the computer, a process which is grossly wasteful of computer time and hampered seriously by the poor console communication usually available. Even if a typewriter is the console, there are usually lacking the sophisticated query and response programs which are vitally necessary to allow effective interaction." - Corbató et al., An Experimental Time-Sharing System

- At one point, what we would now call "I/O" and "CPU" operations were of comparable speed and failure rate. Two decades after ENIAC, however, processing was clearly outpacing I/O. The conception of human-computer interaction changed from interacting with a factory machine to something more like a phone call.
    - "The effect of this time-sharing is to allow a CONVERSATION between the user and the computer, at speeds suitable to the user, and this proves to be one of the most significant features, giving the system great versatility. One effect of this conversational mode of operation is that most interactions involve very small amounts of computer time." - Davies, Proposal for a Digital Communications Network (emphasis mine)

## In the RAND Corporation: Could the 1960s Telephone Network Survive a Nuclear Detonation?

- No.

## How does one create a resilient network?

- Redundancy
  - "We will soon be living in an era in which we cannot guarantee survivability of any single point. However, we can still design systems in which system destruction requires the enemy to pay the price of destroying n of n stations." - Paul Baran, "On Distributed Communication Networks"
  - Interesting sidenote: Baran conceived of an "adversarial model" of error in this paper, where everyday reliability errors are imagined to be created by an intentional adversary.

- But if we're being redundant, maybe we can be cheap and unreliable in normal operation...
  - Baran: "Therefore, we would like to consider the interconnection, one day, of many ALL DIGITAL links to provide a resource optimized for the handling of data for many potential intermittent users..." presenting the message block

- So to Baran, packet switching seems like a natural outgrowth of a distributed, redundant network. But the main focus was still to establish a physical circuit for these switched networks--the primary advantage was interleaving.

## Combining the Two

- ARPA's Information Processing Techniques Office wanted to connect universities supported by its funding together. They contracted Bolt, Beranek, and Newman (BBN) for the job. They were not entirely aware of Baran's work at the start, but the concepts were in the air.
- Larry Roberts deployed a 1200 bps phone line to connect two areas of Lincoln Labs, and everything worked well enough--except for the network itself, which was slow and unreliably. Getting around that constraint signified the main thrust of the ARPANET project.
- A company named BBN came in to connect these machines, developing the IMP (a ruggedized Honeywell mini-computer with telephone modems attached, airlifted into campuses)

## ARPANET and not Internet?

- With time-sharing operating systems, "networks" started to exist--but in an ad-hoc manner. These were not networks as we see today, where each terminal is a computer in itself. Rather, these "networks" were networks of interactive consoles working with a mainframe. Most of the computer power was located on the mainframe, and the terminals were devices mostly capable of connecting to the network.

# Early ARPANET

- Architectural paradigms in the 60s-70s were few and far between. One of the most developed was the master/slave relationship in operating system design. But as the potential of networking changed, old dynamics were already outmoded:
- "You try to connect two such devices together, two computers together, and they only know how to talk to each other as if one is the master. Well, if one is the master, then the other must be the slave. We knew that we wanted a much more flexible vision in which the initiative could be at either site, and there would be a coordinated or cooperative model of communications." - John Crocker @ BBN

- There would big dreams of distributed computing built on top of this tech demo.
- "Those were the days when, instead of viewing the network as an electronic mail system, which was kind of an afterthought in a way, there were all these visions of shared databases and load balancing, or jobs would be shifted from one machine to another."

- Hot-Potato Routing--now a given, but found later justification out of Paul Baran's idea of a network that would have the fewest packets in transit in case of a nuclear war.

- Was ARPANET the first packet switched network? It had packets and switches, but was missing something else we often imply when describing "packet switched networks" - it was not connectionless
- "The ARPA Network is designed on this principle and, at each node, a copy of the message is stored until it is safely received at the following node." - F. E. Heart, "The Interface Message Processor for the ARPA Computer Network"

- ARPANET was NOT end-to-end--it was built off of black-box IMPs, something more like "Gateway-to-Gateway," and established reliable physical circuits that would acknowledge each message over an unreliable network. Universities could not work with these IMPs freely. It was a network for research, not a researchable network. Layers comingled under the management of the IMP.

- Through it all BBN and the ARPA-sponsored universities struggled with each other.
- "In the early days, when they came out with their proposal, we looked in their routing algorithm, which we were very interested in, and said: 'This thing has loops. A packet can go back and forth, or in a circle.' And they said: 'No, there are no loops.' But there are loops! They said: 'No.' So we simulated them and said: 'Look, there's loops.' They said: 'There are no loops.' Then this four node network was implemented and we showed them loops, and the answer was; 'Yes, there are loops.'" - Len Kleinrock

## The End of ARPANET

- An incomplete conclusion could be that the ARPANET was "doomed to fail." It was a network built off of phone lines, paradigmatically designed for reliable routing and poor gateway transparency. However, you could alternatively say that the opposition created between BBN and the academic community, BBN's own confused organization, and the fact that they had to do all of this on 12Kb of memory stunted the full development of the ARPANET.
- Before Open Source was researchability.

## ARPANET to TCP/IP

- Not directly continuous.

- CYCLADES, a project by the French postal service, headed by Louis Pouzin, tried to finish what appeared lacking in ARPANET
- "[BBN] understood that I intended to build another network but they really didn't believe it. They had this feeling that the Arpanet, this kind of complicated system, could only be implemented in a country like the States due to money, expertise and so on. They didn't believe Europe could bring something like that up." - Louis Pouzin

- CYCLADES was an intervening force for who we now credit as the inventors of TCP/IP - Cerf, Kahn, and Metcalfe. CYCLADES had explicit layering by modeling to an application an end-to-end virtual circuit on top of an unreliable, best-effort network. was a cintingently end-to-end network that attempted to be more transparent than the ARPANET. With CYCLADES, modern computing concepts become recognizable 

## End-to-End?

- Why be end-to-end?
    - End-to-end provisioning is useful in that they only need to fix a problem once, at the host, and the host is the device most able to appraise what an error is. Pouzin remained open to non-end-to-end solutions: "With experience gradually building up, and depending on trends in international standards, more stable characteristics will eventually emerge. By putting them at some lower system level, it will be possible to obtain higher efficiency and reduce duplication, at the cost of freezing a few more parameters."
    - However, end-to-end solutions are slow, and not every problem that manifests at the host is more easily solved at the host--(e.g. the rapid adoption of ECN).

- Why use virtual circuits?
    - To Pouzin, freedom in routing packets.
    - "Although various groups call for a DG [datagram] interface, the carriers are opposed to it. Four carriers are rushing a VC [virtual circuit, to Pouzin this means an exclusively carrier-operated network that requires user subscription to that network] protocol through CCITT [Consultative Committee for International Telephony and Telegraphy, a committee in the International Telegraphers Union]. The carrier's goal is to take over terminal handling, and gradually other processing functions. DG's would leave too much freedom to the customer. The political implications of the carrier policy suggest that better boundaries be drawn up between carriers and data processing."

## Conclusion

- Hopefully, this presentation has illustrated that the development of the (more or less) modern internet was not just a rational adoption of design principles, but rather a process that was marked by nuclear war, academic contention, disorganization, and political visions for an ideal internet.
- Apparent "givens" in design like the end-to-end principle and layering were contingents of a decades-long development in human-computer interaction.

## Discussion Questions:
- Is the end-to-end principle still applicable?
- What assumptions made by early designers ended up violated over time, if any?
- Can the internet realistically be changed?

## Sources

- [Paul Baran - On Distributed Communications Networks](https://www.rand.org/content/dam/rand/pubs/papers/2005/P2626.pdf)
- [Fernando Corbato et al. - An Experimental Time-Sharing System](http://larch-www.lcs.mit.edu:8001/~corbato/sjcc62/)
- [Christopher Strachey - Time Sharing in Large Fast Computers](https://ia804601.us.archive.org/0/items/large-fast-computers/Image070917171847.pdf)
- [Donald Davies - Proposal for a Digital Communication Network](https://www.dcs.gla.ac.uk/~wpc/grcs/Davies05.pdf)
- [Larry Roberts - The ARPANET and Computer Networks](https://dl.acm.org/doi/pdf/10.1145/61975.66916)
- [David Clark - The Design Philosophy of the DARPA Internet Protocols](http://ccr.sigcomm.org/archive/1995/jan95/ccr-9501-clark.pdf)
- [James Pelkey - Entrepreneurial Capitalism and Innovation: A History of Computer Communications 1968-1988](https://web.archive.org/web/20210617093154/https://www.historyofcomputercommunications.info/Book/6/6.3-CYCLADESNetworkLouisPouzin1-72.html)
- [Frank Heart et al. - The Interface Message Processor for the ARPA Computer Network](https://www.walden-family.com/public/1970-imp-afips.pdf)
- [Richard Bennett - Designed for Change](https://d1bcsfjk95uj19.cloudfront.net/files/2009-designed-for-change.pdf)
