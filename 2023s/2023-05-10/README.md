# Motivation

- Primary motivation: high-performancecomputing
  - High-performance computing is often computing a [bulk synchronous parallel](https://en.wikipedia.org/wiki/Bulk_synchronous_parallel) algorithm, each worker does one unit of work and waits at a barrier for their peers to also do one unit of work, then repeat. The rate of these algorithms are limited by the slowest worker.
  - Slides 3 -- 11 of <http://users.eecs.northwestern.edu/~kch479/docs/kch-hpdc2015pres.pdf>
    - [Timesharing](https://en.wikipedia.org/wiki/Time-sharing) has unacceptable overhead
    - [Virtual memory mapping](https://en.wikipedia.org/wiki/Virtual_memory) has unacceptable overhead
    - User/kernel context switching has unacceptable overheads
    - Interrupts have unacceptable overheads
- Secondary motivation: Also, Linux has no formal verifiability, not good for safety-critical applications, also hard to make secure enclaves.

# Unikernel solution

- [Unikernel](https://en.wikipedia.org/wiki/Unikernel): "A unikernel is a specialised, single address space machine image constructed by using library operating systems"
  - Library operating system contains the implementation of system operations as a function call instead of a systemcall, assuming the caller is already in kernel mode.
  - Can 'bake' application into a kernel.
  - Application now has unfettered access to the hardware.
  - No user/kernel context switching
- Cons: Can be hard to write
- Unikernel compiler's can help!
  - [MirageOS](https://mirage.io/) compiles OCaml to bare-metal Unikernel
  - [A Unikernel Firewall for QubesOS](http://roscidus.com/blog/blog/2016/01/01/a-unikernel-firewall-for-qubesos/)
    - Very good blog post actually using <1k lines of MirageOS to write a firewall for QubesOS, replacing a 4M LoC Linux VM.

# Hardware partitioning solution

- Instead of dynamically multiplexing applications onto hardware, statically allocate hardware to applications.
- [Exokernel (Wikipedia article)](https://en.wikipedia.org/wiki/Exokernel)
- [Exokernel paper](https://dl.acm.org/doi/10.1145/224056.224076) (1994)
- Can be hard if application doesn't need complex system calls 95% of the time, but 5% of the time needs complex system calls or device I/O that is only implemented in Linux.
  - [Lightweight Kernel Operating System (Wikipedia article)](https://en.wikipedia.org/wiki/Lightweight_Kernel_Operating_System)
    - "A new direction for lightweight kernels is to combine them with a full-featured OS, such as Linux, on a many-core node. These multikernel operating systems run a lightweight kernel on some of the CPU cores of a node, while other cores provide services that are omitted in lightweight kernels. By combining the two, users get the Linux features they need but also the deterministic behavior and scalability of lightweight kernels."
    - Also called "co-kernels", since they co-operate.
    - Need a virtual machine monitor (like a hypervisor) to split up the hardware and facilitate secure kernel-to-kernel interaction.
  - [What is a Lightweight Kernel](http://users.eecs.northwestern.edu/~kch479/docs/riesen-lwk.pdf)
- Rest of <http://users.eecs.northwestern.edu/~kch479/docs/kch-hpdc2015pres.pdf>
- [Remote attestation](https://en.wikipedia.org/wiki/Trusted_Computing#REMOTE-ATTESTATION) gives us a novel secondary motivation for research co-kernels: Linux (big and not trusted, but has complex device drivers) can be driven by Lightweight kernel (small and trusted, but no device drivers).
- State of the art:
  - [Palacios Virtual Machine Monitor](http://www.v3vee.org/palacios/)
  - [https://github.com/HobbesOSR/kitten](Kitten lightweight kernel)
  - [https://github.com/HExSA-Lab/nautilus](Nautilus lightweight kernel)
