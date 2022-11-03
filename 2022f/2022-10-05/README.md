---
title: GNULUG Oct 5 meeting: FUSE!
author: Samuel Grayson
########
# Note #
########
# You can read this file in plaintext or you can render it with `pandoc --standalone --to revealjs --output index.html README.md`
---

# First, projects

- Evan: <https://github.com/evidlo/nanpa_lookup>

# Monolithic, modular, or microkernel?

# Monolothic

- All important operations implemented in kernelspace and at install time.
- Possibly layered
- E.g. Windows, FreeBSD

--------

![](https://upload.wikimedia.org/wikipedia/commons/5/5d/Windows_2000_architecture.svg)

# Modular

- All important operations implemented in kernelspace, but you can add/remove modules from the kernel.
- More similar to monolothic, just with module load/unload.
- E.g. Linux

--------

![](https://i.imgur.com/Oufl1R1.png)

# Microkernel

- Most important operations implemented in userspace, installed/removed like users programs.
- E.g. MINIX, GNU HURD

--------

![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/OS-structure.svg/1280px-OS-structure.svg.png)

# Kernel- vs user-space

- In userspace, a CPU register makes certain assembly instructions illegal.
- In kernelspace, that register is off => direct control over hardware.
- Kernelspace > root user > normal user

--------

![](https://i.imgflip.com/6vwudc.jpg)

# Kernel- vs user-space

- Kernelspace requires a greater degree of trust. Becomes attack surface for hackers.
- Why not implement operation in userspace? Direct hw access and performance. For file systems, mostly performance.
  - Kernel please read this big file into my memory space.

# Linus vs Tanenbaum debate

- [Mailing list archives](https://web.archive.org/web/20121003060514/http://www.dina.dk/~abraham/Linus_vs_Tanenbaum.html)

--------

![](https://i.imgflip.com/6vvwfh.jpg)

# FUSE

- Filesystem in User SpacE
- Inspired by GNU HURD
- For FS that isn't performance critical or system critical

# Examples

- [Autotier FUSE](https://github.com/45Drives/autotier) that automatically moves files into tiered storage based on access.
- [SSHFS](https://en.wikipedia.org/wiki/SSHFS) mounts a directory on a remote over SSH. Needs a maintainer!
- [rclone mount](https://rclone.org/commands/rclone_mount/) lets you mount Google Drive (!)

# Our FUSE

```
$ mkdir test
$ # install by system package manager and call "make" or use Nix to install and compile
$ nix build .
$ ./result/bin/vanilla_fs test
<lots of output>
$ # in another terminal
$ ls -l test
total 0
-rwxrwxrwx 0 root root 29 Dec 31  1969 every_path_resolves_to_a_file
-rwxrwxrwx 0 root root 29 Dec 31  1969 welcome_to_bbfs
```

--------

[asciicast](https://asciinema.org/a/1SYKFtKmWS3nJVqmsEdqyZ76c)

<script id="asciicast-1SYKFtKmWS3nJVqmsEdqyZ76c" src="https://asciinema.org/a/1SYKFtKmWS3nJVqmsEdqyZ76c.js" async></script>

# Our FUSE

- Trial-by-error: you need `getattr` for anything else to work.
- `getattr` must set `st_mode = S_IFDIR` for files and `st_mode = S_IFREG` for anything else to work.
- `getattr` must set `st_size` to the real size of the file. GLIBC read will truncate the result to this size!
- `write` returns the number of bytes written. This must equal the number of bytes requested (third arg) or else GLIBC will think that `write` failed.

# Our FUSE (continued)

- `read` takes an optional offset, which begins reading from that point.
- `read` must return the number of bytes read. If this is less than the amount requested, GLIBC interprets this as the end-of-file.
- `readdir` calls `filler(...)` to return results

# Your FUSE

- [FUSE documentation](https://www.cs.hmc.edu/~geoff/classes/hmc.cs135.201109/homework/fuse/fuse_doc.html)
  -  Fuse options `-s`: single-threaded, `-d`: debug mode (implies `-f`), `-f`: foreground.
  - Can leave almost any methods unimplemented.
- [Nice FUSE tutorial](https://www.cs.nmsu.edu/~pfeiffer/fuse-tutorial/html/index.html)
- Try starting from a ['passthrough' FUSE](https://github.com/libfuse/libfuse/blob/master/example/passthrough_fh.c) that proxies the underlying FS?
