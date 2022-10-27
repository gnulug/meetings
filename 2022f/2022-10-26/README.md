---
title: "The syscall of the wild"
---

The Syscall of the wild

<img src="https://mpd-biblio-covers.imgix.net/9780812504323.jpg?w=900" style="height: 35vw;" />

Compile me with `make README.html`

---------

- Diff between function call and syscall?
- `test.c` and `test.s`
- `asm("nop; nop;");` creates a "bookmark" in the asm output.
- How to clobber memory? `asm(:: "memory");`

# Function Call

```asm
mov    $0xe,%ecx
lea    0x0(%rip),%rbx # 18 <main+0x13>
mov    %rbx,%rdx
mov    $0x1,%esi
mov    $0x1,%edi
call   2a <main+0x25>
```

# Syscall

```asm
mov    $0x1,%eax
mov    $0xe,%edx
mov    %eax,%edi
mov    %rbx,%rsi
syscall 
```

# Why do we need syscalls?

- Security

# Libc

- <https://www.etalabs.net/compare_libcs.html>

# vDSO

- Why is switching to kernel-space slow?
- Is it necessary all the time?
- Enter: vDSO

# vDSO Security

- Return-to-libc
- [ASLR](https://en.wikipedia.org/wiki/Address_space_layout_randomization)

> Calling the old vdso "UNSAFE" as a config option is just plain stupid. It's a politicized name, with no good reason except for your political agenda. And when I call it out as such, you just spout the same tired old security nonsense. 

# Tiny binaries

- Use raw syscalls -> no need for libc.

- ```C
__attribute__((force_align_arg_pointer))
void _start() {
	...
	__builtin_unreachable();
}
```

- also `-strip` and `-Os`
