# UIUC GNULUG

Meeting info on [website](https://lug.acm.illinois.edu/)

# Possible project proposal?

- https://github.com/charmoniumQ/merkle-tree-file-system

# How the UNIX Shell works (Sam)

- `fork()` and `execve()` syscalls
- `/usr/bin/[` is just a symlink to `/usr/bin/test`
  - `/usr/bin/[`, `1`, `=`, `2`, `]` returns 1
  - `/usr/bin/[`, `1`, `=`, `1`, `]` returns 0
```
$ echo -e '#!/usr/bin/env python\nimport sys; print(sys.argv)' > script.py
$ chmod +x script.py
$ a='1 2 3'
$ ./script.py $a
["./script.py", "1", "2", "3"]
$ ./script.py $a
["./script.py", "1 2 3"]
```
- Bash re-reads the script _as it is executing!_
- [Unix Haters Handbook](https://web.mit.edu/~simsong/www/ugh.pdf) page 147
- Examples: https://samgrayson.me/2021-01-01-shell/

# Fish shell (Russel)

- https://fishshell.com/
- Good defaults
- Tab-completes options from man-page
- Fish automatically searches for previous commands
- Zsh shell can try to have the same features, not as good.
  - https://github.com/marlonrichert/zsh-autocomplete
  - https://github.com/zsh-users/zsh-syntax-highlighting
  - Not default! Zsh users have to configure!

# Oil shell (Evan)

- https://www.oilshell.org/
- Better for-loop syntax
- Better variable syntax

# Ammonite shell (Sam)

- Slides: https://docs.google.com/presentation/d/11vZzXCfAA0aOFAuHA0nAvAzALGFGCH-dqHxx6XMgbk8
- Shell underlies important applications/orchestration but has low guarantees! (no typesafety)
- But at least it's concise? Safer alternatives are very verbose (Python, Java, Scala)
- Develop a Scala library to make it less verbose (still using Scala REPL)
- Develop a Scala REPL suitable for system shell.
  - No more than twice as verbose as Bash.
