---
title: "Tracing the syscall of the wild"
---

# Tracing the syscall of the wild

<img src="https://mpd-biblio-covers.imgix.net/9780812504323.jpg?w=900" style="height: 35vw;" />

--------

Compile me with `pandoc --standalone --to=revealjs --output=README.html README.md`

Env for demos can be prepared by `nix develop` or `nix develop --command $SHELL`

--------

# Miscellany

- Meeting time conflicts with ACM x WCS
- GLUG/ACM cloud??

---------

# Debugging with strace

- Create new process (`strace $cmd`) or attach to existing one (`strace -p $pid`)

- Filter by syscall (`--trace=openat`) or group of syscalls (`--trace=%file`)

--------

```
$ strace --follow-forks --trace=%file --output=log ls
...

$ cat log
...
openat(AT_FDCWD, ".", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 3
```

--------

```
$ strace --follow-forks --trace=%file --output=log ls -l
...

$ cat log
...
openat(AT_FDCWD, ".", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 3
statx(AT_FDCWD, "spack.yaml", ...) = 0
many times
```

- ["statx() v3" on LWN](https://lwn.net/Articles/707602/)

---------

```
$ strace --follow-forks --trace=openat --output=log zsh -c 'echo hi'
hi

$ cat log
...
openat(AT_FDCWD, "/etc/passwd", O_RDONLY|O_CLOEXEC) = 11
openat(AT_FDCWD, "/etc/zshenv", O_RDONLY|O_NOCTTY) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/home/sam/.zshenv", O_RDONLY|O_NOCTTY) = 3
openat(AT_FDCWD, "/home/sam/.config/zsh/.zshenv", O_RDONLY|O_NOCTTY) = 3
openat(AT_FDCWD, "/home/sam/.nix-profile/etc/profile.d/hm-session-vars.sh", O_RDONLY|O_NOCTTY) = 3
openat(AT_FDCWD, "/dev/null", O_RDONLY|O_NOCTTY) = 3
```

--------

# rr debugger

- [Website](https://rr-project.org/)
- [Technical paper](https://arxiv.org/pdf/1705.05937.pdf)
- Record and reply programs
  - Works on Firefox!

--------

```
$ python -c "import random; print(random.choice(range(100)))"
39

$ rr record python -c "import random; print(random.choice(range(100)))"
rr: Saving execution to trace directory `/home/sam/.local/share/rr/python-5'.
59

$ rr replay --autopilot /home/sam/.local/share/rr/python-5
59

$ rr dump /home/sam/.local/share/rr/python-5 > log

$ less log

```

--------

# CDE

- [Technical paper](https://www.usenix.org/events/atc11/tech/final_files/GuoEngler.pdf)

--------

# VM

- Full system simulation vs syscall emulation in Gem5
  - [syscall table](https://github.com/gem5/gem5/blob/5de8ca95506a5f15bfbfdd2ca9babd282a882d1f/src/arch/arm/linux/process.cc#L127)
  - [implementation of emulation](https://github.com/gem5/gem5/blob/7b9364b5c0e0a211449c2974c31f9c5a4176557d/src/sim/syscall_emul.hh#L2622)

--------

# Hybrid Runtime

<img src="./hybrid_runtime.png" style="height: 35vw;" />

--------

# Hybrid Runtime

- Turn off interrupts
- Use hugepages
- No scheduler
- Let Linux handle FS

--------

# Nautilus (hybrid runtime)

```
$ make menuconfig
# exit, saving config

$ make isoimage
```

--------

# Performance engineering

- Strace has wicked overhead because switch processes every traced syscall.
- How to avoid? => Write filtering logic in kernel??
- eBPF := a restricted language, safe to execute within kernel!
- Implement filtering logic in eBPF

--------

- <https://brendangregg.com/ebpf.html>

--------

# Future topics

- Hybrid runtime research
- Security auditing research
- Linux performance tuning
  - Karaoke anything [Brendan Gregg](https://brendangregg.com/) has ever written
  - [Debugging ZFS performance](https://brendangregg.com/blog/2021-09-06/zfs-is-mysteriously-eating-my-cpu.html)
