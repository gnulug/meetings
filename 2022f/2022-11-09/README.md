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

--------

# Syscalls

- `open(...)`
- `read(...)`
- `write(...)`
- `close(...)`
- `fork(...)` sometimes implemented as `cone(...)`
- `exec`-family

# Program

See `./test2.c`.

# Strace

```
$ ./test2.c
$ strace --follow-forks ./test2.exe README.md readme2
...
openat(AT_FDCWD, "README.md", O_RDONLY) = 3
openat(AT_FDCWD, "readme2", O_WRONLY|O_CREAT|O_TRUNC, 0644) = 4
read(3, "---\ntitle: \"Tracing the syscall "..., 1024) = 764
write(4, "---\ntitle: \"Tracing the syscall "..., 764) = 764
write(1, "Copied 1 partial block\n", 23) = 23
write(1, "Copied 764 bytes in total\n", 26) = 26
...
clone(...)
...
[pid 1892568] execve("/bin/ls", ["."], ...) = 0
...
[pid 1892568] openat(AT_FDCWD, ".", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 5
...
[pid 1892568] write(1, "log  readme2  README.md  test  t"..., 49) = 49
...
<... wait4 resumed>[{WIFEXITED(s) && WEXITSTATUS(s) == 0}], 0, NULL) = 1892568
write(1, "ls done\n", 8) = 8
```
