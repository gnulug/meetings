# NetworkManager (Krishnan)

# eBPF (Sam)

- Upload code to the kernel, to run at kernel-level.
  - The code is written in a restricted language, eBPF, so that it can be formally verified (halting, no memory leakage, etc.).
  - Need root and `CAP_EBPF` (not usually given inside containers)
  - Make performance observations, security auditing, and even access control rules (seccomp-bpf which uses un-extended BPF)
  - Kernel has hooks that call into eBPF, and you can only 'change' behavior by installing functions at those hooks.
    - Can't implement a new syscall through eBPF, for example
- [Overview](https://ebpf.io/what-is-ebpf/)
- [Formal description](https://arxiv.org/pdf/2410.00026)
- eBPF is a byte-code language (think JVM bytecode), so you usually want some kind of front-end.
  - [Different frontends by difficulty, capability, and maturity](https://www.brendangregg.com/ebpf.html#frontends)
- Bpftrace
  - bpftrace strikes a good balance between capability and ease-of-use.
  - bpftrace is a language structured like Awk (event-based).
  - Can't really define new functions, but some functions are builtin.
  - Builtin maps/dicts
  - [examples](https://bpftrace.org/tutorial-one-liners)
- Careful on clouds! if they give you CAP_BPF
  - If your performance tools all depend on eBPF, you can't easily use them in containers without CAP_BPF.
  - But CAP_BPF breaks container abstractions
  - https://www.usenix.org/system/files/usenixsecurity23-he.pdf
- Access control with BPF
  - Instead of rwx bits and users, you may want to write a small program that decides if some syscall by some user on some object is dis/allowed.
  - Greatly increases "dynamism", like how JavaScript makes the Web dynamic.
  - But that language should be restricted, bounded time, bounded memory, etc., so seccomp uses BPF (not extended eBPF).
  - [Writing/installing a BPF seccomp filter in C](https://sh4dy.com/2024/04/08/seccomp-bpf/)
    - ```c
    #include <stdio.h>
    #include <stdlib.h>
    #include <stddef.h>
    #include <unistd.h>
    #include <linux/audit.h>
    #include <linux/filter.h>
    #include <linux/seccomp.h>
    #include <sys/mman.h>
    #include <sys/prctl.h>
    #include <sys/syscall.h>
    
    #define BLOCK_SYSCALL(syscall)                                 \
        BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K, __NR_##syscall, 0, 1), \
        BPF_STMT(BPF_RET | BPF_K, SECCOMP_RET_KILL)
    
    struct sock_filter filter[] = {
        // Validate architecture
        BPF_STMT(BPF_LD | BPF_W | BPF_ABS, offsetof(struct seccomp_data, arch)),
        BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K, AUDIT_ARCH_X86_64, 1, 0),
        BPF_STMT(BPF_RET | BPF_W, SECCOMP_RET_KILL),
    
        // Load the system call number
        BPF_STMT(BPF_LD | BPF_W | BPF_ABS, offsetof(struct seccomp_data, nr)),
    
        // Block system calls
        BLOCK_SYSCALL(mmap),
        BPF_STMT(BPF_RET | BPF_W, SECCOMP_RET_ALLOW),
    };
    
    struct sock_fprog prog = {
        .len = (unsigned short)(sizeof(filter) / sizeof(struct sock_filter)),
        .filter = filter,
    };
    
    void fatal_error(const char *message) {
        fprintf(stderr, "%s\n", message);
        exit(1);
    }
    
    int main() {
        if (prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0)) {
            perror("prctl(PR_SET_NO_NEW_PRIVS) failed");
        }
        if (prctl(PR_SET_SECCOMP, SECCOMP_MODE_FILTER, &prog) == -1) {
            perror("prctl(PR_SET_SECCOMP) failed");
        }
        mmap(0, 0x1000, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_ANONYMOUS | MAP_PRIVATE, -1, 0);
        return 0;
    }
    ```
  - [Classic BPF vs eBPF](https://www.kernel.org/doc/html/latest/bpf/classic_vs_extended.html)
  - [This paper](https://arxiv.org/pdf/2302.10366) proposes using extended eBPF
