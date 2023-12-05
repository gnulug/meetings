# Puppet

> “From a drop of water…a logician could infer the possibility of an Atlantic or a Niagara without having seen or heard of one or the other.
>
> &mdash; <cite>Sherlock Holmes, A Study in Scarlet</cite>

-   In a similar fashion, any astute inquirer may start with a single piece of creative output and find their bearings an entirely new field of thinking.
    
Ergo,

# Puppet

A software *system*. Or, in it's own words, a "system configuration management tool.

* Disclaimers: or what this presentation won't be
	* A rigorous tutorial - Look online. People have been paid to make content on this. RTFM.
	* Useless - Given that, this presentation should give those tutorials some enhanced relevance
	* Solely about Puppet - If it's not a tutorial, there's room for a broader scope.
	* Purely factual - **¯\\_(ツ)_/¯**

### Puppet Biography

* Started by Luke Kanies in 2004
	* A sysadmin who "learned to be a programmer" while creating Puppet
* Licensed as "open-core"
	* Apache core with Proprietary extensions (including a **GUI**)
* Currently owned by Perforce
	* Laid off 75 of 500 employees after acquisition in April 2022
---
* Lineage
	* **C**on**F**iguration **E**ngine aka CFEngine
		* Created by Mark Burgess circa 1993
	* IsConf v3 written by Kanies circa 2002
	* Notably the tools came before the theory was formalized, or existed.
	* Take a historical look (the same as the authors)

---

* History
	* Novell, Workgroups for Windows, Sun Microsystems (RIP)
	* 1998 - ["Bootstrapping an Infrastructure"](https://www.usenix.org/legacy/publications/library/proceedings/lisa98/full_papers/traugott/traugott.pdf) by Steve Traugott
		* Based on the previous four years work as NASA
		* A recipe for success, and not irrelevant today imo
	* Big idea : the infrastructure is one coherent machine, an "enterprise virtual machine"
	* "The couple on the system" had remained, but it had loosened as evidenced by the modularity of the parts

### Systems Theory

* Systems administration has found a market rationale.
	* As much a science as computer science [Burgess 3]
	* Undeniably a branch of engineering [Burgess 1]
	* Similar to any operational position, it only comes to the fore in an org when [things go wrong](https://www.wired.com/story/notpetya-cyberattack-ukraine-russia-code-crashed-the-world/)

---

* When things go right: An ideal world
	* Three points/truths/koans of the field are apparent:
		1. Policy : aims & wishes, human-readable and machine -readable, what we want & how things should be [Burgess 76]
			* E.g. Deny undergrads their certain unalienable right to free printing
		2. Predictable : Reason about the state of the system
			* A defined "good" state defines reliability
		3. Scalable : Systems that remain predictable as they grow in size [Burgess 7]

---

* Definitions
	* System - systematic, meaning certain stimuli, there are certain expected responses
	* Deterministic - Those certain expected responses
	* Nested - A subsystem within a larger system, which is itself part of a larger system, compare *holonarchy*
		* Nodes of computers -> easy
		* Nodes of people -> not so easy (see [BOFH](https://en.wikipedia.org/wiki/Bastard_Operator_From_Hell))
	* Nodes have to balance uniformity and variety
		* More uniform -> Better static predictability
		* More variety -> Minimize loss potential ("hedge your bets" & Murphy's law)
	* Analyzing uniformity & variety apply at any level of the model, or any arbitrary model at all (e.g. networks, large systems, etc.)

---

Models for applying change (see [the video](the video))
* push/pull
* Divergence/Confluence/Congruence
EXIT METHOD Systems Theory

---

["Why Order Matters" by Steve Traugott](https://www.usenix.org/legacy/publications/library/proceedings/lisa02/tech/full_papers/traugott/traugott_html/index.html) pub. December 2002
* Had found success repeatedly and with increaing effectiveness
	* Fast rollouts and industry adoption
* Naturally, they wanted to know **why?** And crucially, how to *prove* their superiority to their peers.
* Intuition: Contra many of their peers, the ordered deterministic nature of the toolset granted success

### Today and beyond

* NixOS -> A congruent model
* What about databases? Is confluence enough?
* What about regulators or outside audits?
* Amazon AMI?



