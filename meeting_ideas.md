- Self-hosted
  - Mosh
  - Router security
  - Router port forwarding
  - Docker compose vs Swarm vs Kubernetes
  - Dynamic DNS
  - ddclient
  - Traefik vs NGINX vs HAProxy
  - Letsencrypt
  - httpbin
  - HTTP basic auth vs Google OAuth
  - SQL Databases (MySQL, MariaDB, PostgreSQL, SQLite)
  - pwgen

































- General
  - https://www.win.tue.nl/~aeb/linux/lk/lk.html
- Async I/O
  - https://libevent.org/
  - https://github.com/thlorenz/libuv-dox
  - http://www.kegel.com/c10k.html
  - http://www.citi.umich.edu/projects/linux-scalability/reports/accept.html
- Threads
  - https://akkadia.org/drepper/nptl-design.pdf
  - https://akkadia.org/drepper/glibcthreads.html
  - https://dl.acm.org/doi/abs/10.1145/146941.146944
  - https://dl.acm.org/doi/abs/10.1145/121132.121115
- Select
  - https://idea.popcount.org/2016-11-01-a-brief-history-of-select2/
  - https://idea.popcount.org/2017-01-06-select-is-fundamentally-broken/
  - https://idea.popcount.org/2017-02-20-epoll-is-fundamentally-broken-12/
  - https://idea.popcount.org/2017-03-20-epoll-is-fundamentally-broken-22/
  - https://idndx.com/the-implementation-of-epoll-1/
- Dotfiles session
  - Editors
    - https://missing.csail.mit.edu/2020/editors/
  - Shells
  - Terminal multiplexers
    - https://reddit.com/r/unixporn
- Virt memory
  - `/proc/$PID_OR_SELF/maps`
  -
  ```
<address start>-<address end>  <mode>  <offset>   <major id:minor id>   <inode id>   <file path>
559b8c418000-559b8c41a000      r--p    00000000          08:30               1708     /usr/bin/cat
```
  -
```
import re, pathlib, collections, shlex
shared_paths = {}
for proc_dir in pathlib.Path("/proc").iterdir():
    if re.match("[0-9]+", proc_dir.name) and (proc_dir / "maps").exists():
        try:
            map_text = (proc_dir / "maps").read_text()
        except PermissionError:
            pass
        else:
            # yay, the read_text succeeded
            proc_name = shlex.join((proc_dir / "cmdline").read_text().split("\x00"))
            this_shared_paths = set()
            for line in map_text.strip().split("\n"):
                m = re.match("([a-z0-9]+)-([a-z0-9]+) +([a-z-]{4}) +([0-9a-z]+) +([0-9a-z]+):([0-9a-z]+) +([0-9]+) +([^ ].+|)", line)
                if m is not None:
                    addr_begin, addr_end, mode, offset, major, minor, inode, path = m.groups()
                    path = path.partition(" ")[0]
                    if mode[3] == "s":
                        shared_paths.setdefault(path, set()).add(proc_name)
                elif line.strip():
                    print("Failed to parse:", line)
k = 10
print("printing top", k, "shared libraries")
for path in sorted(shared_paths, key=lambda path: len(shared_paths[path]), reverse=True)[:k]:
    processes = shared_paths[path]
    print(path, "is used by", len(processes), "processes")
    for process in processes:
        print("  ", process)
    print()
```
  - Contiguity
  - write xor execute
  - private xor shared
  - Dynamic library loads
  - Query dynamic library sharing?
  - Fragmentation
  - ELF specification
- Remote access
  - SSH
    - keys
    - ~/.ssh/config
    - /etc/sshd/config
    - Debugging
  - Mosh
  - Port forwarding
  - ngrok
  - Tmux pair coding
- Desktop and GUIs
  - RDP (on our cluster?)
  - Lightest possible desktop env competition
- Open source software revolution
  - OSS revolution. Computing for users not corporations
  - SIG POL
  - History of Stallman and the FSF
    - Free as in speech vs free as in beer
    - Copyleft
    - MPL vs LGPL vs GPL
    - Proprietary BLOBs in Linux
    - Proprietary firmware
  - RevolutionOS
  - Open hardware
  - Opencola/Freebeer
  - Creative Commons
    - Blender movies
    - Music
  - Open standards
    - Ogg, Vorbis, Matroska, Webm, PNG
  - Linked data
    - https://www.w3.org/DesignIssues/LinkedData.html
  - US sanction on tornado cash
  - Totalitarian governments
  - Aaron Swartz
  - CSS
- Containers and virtualization
  - Virtual machines vs containers
  - Virtual machines
    - VirtualBox
    - QEMU
    - Vagrant
  - Containers
    - Nix
    - Docker
      - Namespaces
        - https://website.peterjin.org/wiki/Notes_about_namespaces
        - https://en.wikipedia.org/wiki/Linux_namespaces
        - https://en.wikipedia.org/wiki/Plan_9_from_Bell_Labs
        - https://github.com/lethalman/nix-user-chroot/blob/master/main.c
      - cgroups
    - Podman
    - OCI
    - systemd containers
    - BSD jail
- DevOps
  - Use case for AWS/GCP/Azure/Openstack services
  - Experiment on our Openstack?
  - Terraform
  - Helm
  - Compute resource managers
    - Docker compose
    - Docker swarm
    - k8s
  - Google SRE book
  - Cool systems
    - Ceph
    - IPFS
    - Hadoop
    - Spark
    - Dask
  - Explain data sharding
- What is compiler bootstrapping?
  - Reflections on Trusting Trust
  - LLVM
  - https://guix.gnu.org/blog/2018-bootstrapping-rust/
  - Cross-compiling
  - PyPy
- Distributed computing
  - Schedulers
    - k8s
    - Slurm
    - Hadoop
    - Spark
    - Dask
  - Get time on campus cluster?
  - Mirai botnet
  - Processing big data processing on Linux
    - Go through EDGAR-analysis
    - Dask
    - Slurm
    - k8s
    - S3
    - charmonium.cache
- Do together: Set up Minecraft server
- Do together: Set up personal media server
  - Music
    - Do first, use in background for rest of meeting
  - Movies/TV
    - Wargames
    - https://www.blender.org/about/studio/
    - Silicon Valley
- Do together: Setup a Matrix <-> {Discord, IRC, ...}
  - Client
  - Server
- Do together: Pi-hole
  - DNS
  - Pinhole
- Linux games
  - Sauerbraten
  - Minecraft
- Cybersecurity
  - Famous examples
    - Mirai botnet
    - Stuxnet
- Distributed network
  - WWW
    - Mastedon
    - Diaspora
    - Micropub
    - Indieweb
    - https://www.w3.org/DesignIssues/LinkedData.html
  - Scuttlebutt
  - IPFS
  - Bittorent
  - TOR
- Personal security
  - Personal security
  - Yubikey vs HOTP vs TOTP
  - Full disk encryption
  - GPG
    - Just signing/verifying a file from command line
    - Thunderbrid + GPG
    - Git + GPG
    - Keybase
  - SIG PWNY
  - TOR vs VPN
  - Torrenting safely
    - https://security.stackexchange.com/questions/129762/is-malware-distributed-with-pirated-software-actually-common
  - Amnesic Live OS (Tails)
  - How to set up and use dead drops (like Wikileaks)
- Shell usage and scripting
  - https://github.com/gnulug/cli-cheatsheet
  - Scrpiting pitfalls
    - `test` or `[`
    - Why quotes around variable
    - Why braces around variable
    - Bash variable substitutions
    - Subshells
    - Functions
    - Portability
      - Bash: `$(())`
      - Bash: `[[`
    - `set -eoux NOUNSET PIPFAIL`
    - `set +x`
    - `cd $(dirname $0)`
    - https://samgrayson.me/2021-01-01-shell/
    - https://missing.csail.mit.edu/2020/shell-tools/
    - https://missing.csail.mit.edu/2020/data-wrangling/
  - https://missing.csail.mit.edu/2020/command-line/
  - Unix Readline
  - Alternative shells
    - Ammonite
    - Xonsh
- Systems researchers
  - Tianyin Xu or students
  - Microkernels, GNU Hurd, FUSE
  - Novel virtual memory schemes
  - Elastic Cuckoo page tables
- threads in the kernel
  - Scheduler activations
  - M:N threading
  - Pthreads
  - In other kernels
- The Loader
  - http://netwinder.osuosl.org/users/p/patb/public_html/elf_relocs.html
- Systems tools
  - ELF
  - DWARF
  - https://github.com/ajaymt/thorin
  - ldd and `LD_LIBRARY_PATH`
  - strace, ptrace
- How to debug system software
  - `set -eoux NOUNSET PIPFAIL`
  - ldd and `LD_LIBRARY_PATH`
  - `objdump`, `elfdump`, and `readelf`
  - `dmesg` and `journalctl`
  - strace, ptrace
  - gdb
  - `-g` builds
  - `env`
  - https://missing.csail.mit.edu/2020/debugging-profiling/
  - GitHub issues
  - E.g.
    - https://github.com/spack/spack/issues/30373
    - https://github.com/spack/spack/pull/30418
    - https://github.com/dimitri/el-get/pull/2865
- Kernel security and research
  - SIG PWNY
  - ASLR and KASLR
- Do together: Implement a FUSE
- Do together: Implement a syscall
- Git session
  - git config
  - gitflow
  - git bisect
  - SRE thoughts
    - Continuous integration
  - GitHub pull requests
- Data backups?
  - rsync
  - rclone
- Do together: server security
  - https://github.com/gnulug/website/blob/master/presentations/security/index.html
  - SIG PWNY
  - sshd security
    - Only ssh user group, not root
    - Disable password login
    - Complex logon protocols like SSO and 2FA
    - Discuss alternative ports, port knocking
  - fail2ban
  - Monitoring
    - Grafana
    - Nagios
- Writing in Linux
  - Features:
    - Plaintext (Git tracked)
      - Separate style from content
    - Rich vs plain text
    - Programmable
        - Bibliography management
  - Presentations
    - Revealjs
      - Markdown
    - Beamer + LaTeX
  - Writing
    - Markdown
    - LaTeX
    - Pandoc
- Writing CLIs
  - https://samgrayson.me/2021-01-01-shell/
    - https://clig.dev/
    - Typer, Typer-rich
- Sysadmin careers
  - SRE
  - DevOps
    - Ops
    - Sysadmin
    - SWE
  - Guest speaker?
- History of UNIX
- Non-Linux Unixes?
  - OpenBSD
  - MINIX
  - Dragonfly BSD
  - Plan 9
- Writing opensource packages
  - Do together?
  - Nix
  - Guix
  - Spack
- Previous meetings
  - https://github.com/gnulug/website/tree/master/guides
  - https://github.com/gnulug/website/tree/master/presentations
