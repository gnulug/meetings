---
title: "Containers: namespaces and cgroups"
---

Compile me with:

```
pandoc --standalone --to=revealjs --output=README.html README.md
```

---

# Preliminaries

## History of OS

1. Early computers: only run one prog
1. Batch machines?
2. Invent CPU scheduling:
   - we don't want to waste cycles when a job is waiting on I/O.
3. Invent (isolated) virtual memory:
   - process shouldn't have to care what addresses other processes use.

## What is an OS

**To securely and fairly allocate physical resources to multiple tasks**

- Secure, one task can't access another's resources (on accident or on purpose).
- Fair, everybody should get something, in proportion to the user's wants.

## Deficiencies

1. Performance isolation not really guaranteed.
   - DoS possible (forkbomb, also legit progs)
2. Invent hypervisor: Run everything in VMs
3. Hypervisor and kernel both do same work (scheduling, virt mem)
4. Each abstraction layer introduces overhead. Should be able to do this with one kernel?
5. Invent namespaces and cgroups in Linux kernel.

## What is a container?

- Isolate resource names
  - `/bin/bash` in the container != `/bin/bash` on the host
  - `PID 1` in the container != `PID 1` on the host
- Bound resource utilization (CPU and mem)

# Namespaces

## What are namespaces

- Like namespaces in C++
- Mount
- UTS namespaces (uname)
- IPC namespaces (shouldn't IPC be files?)
- PID namespaces
- Network namespaces
- User namespaces
- [More info on LWN](https://lwn.net/Articles/531114/#series_index)

## How to use namespaces?

- Create & join new NS when starting a process (`clone()`)
- Join existing after starting a process (`setns()`)
- Create & join new NS after starting a process (`unshare()`)

## User namespaces (id map)

```sh
$ id
uid=1000(sam) gid=100(users) groups=100(users),1(wheel)

$ unshare --user --map-users=2000:1000:1 --map-groups 200:100:1 /bin/sh
sh-5.2$ id
uid=2000 gid=200 groups=200,65534(nogroup)
```

## User namespaces (test)

```sh
$ ls -l /proc/self/ns/user
lrwxrwxrwx 1 sam users 0 Feb 19 15:26 /proc/self/ns/user -> 'user:[4026531837]'

$ unshare --user /bin/sh             
sh-5.2$ ls -l /proc/self/ns/user
lrwxrwxrwx 1 nobody nogroup 0 Feb 19 15:26 /proc/self/ns/user -> 'user:[4026533805]'
```

## User namespaces (files host → container)

```
```sh
$ id
uid=1000(sam) gid=100(users) groups=100(users),1(wheel)

$ touch test

$ stat test | grep Uid
Access: (0644/-rw-r--r--)  Uid: ( 1000/     sam)   Gid: (  100/   users)

$ unshare --user --map-users=2000:1000:1 --map-groups 200:100:1 /bin/sh
sh-5.2$ stat test | grep Uid
Access: (0644/-rw-r--r--)  Uid: ( 2000/ UNKNOWN)   Gid: (  200/ UNKNOWN)
```

## User namespaces (files container → host)

```sh
$ id
uid=1000(sam) gid=100(users) groups=100(users),1(wheel)

$ unshare --user --map-users=2000:1000:1 --map-groups 200:100:1 /bin/sh
sh-5.2$ touch test
Access: (0644/-rw-r--r--)  Uid: ( 2000/ UNKNOWN)   Gid: (  200/ UNKNOWN)

sh-5.2$ exit

$ stat test | grep Uid
Access: (0644/-rw-r--r--)  Uid: ( 1000/     sam)   Gid: (  100/   users)
```

## "Unprivileged namespaces"

> starting with Linux 3.8, unprivileged processes can create user namespaces in
> which they have full privileges, which in turn allows any other type of
> namespace to be created inside a user namespace.

- Root in the ns, no privs outside of it (king of your backyard)

## User namespaces (becoming root)

```sh
$ unshare --user --map-users=0:1000:1 --map-groups 0:100:1 /bin/sh
sh-5.2# id
uid=0(root) gid=0(root) groups=0(root),65534(nogroup)

sh-5.2# echo >> /etc/passwd
sh: /etc/passwd: Permission denied

sh-5.2# stat /etc/passwd | grep Uid
Access: (0644/-rw-r--r--)  Uid: (65534/  nobody)   Gid: (65534/ nogroup)
```

## Mount namespaces

- Propagation type: "whether mount points created/removed under this mount point are propagated to other mount points"
  - shared > slave > private > unbindable

```sh
$ wget https://dl-cdn.alpinelinux.org/alpine/v3.19/releases/x86_64/alpine-standard-3.19.1-x86_64.iso
$ mkdir root
$ tar --extract --file=alpine-minirootfs-3.13.1-x86_64.tar.gz --directory root
$ unshare --user --mount --root root /bin/sh
~ $ /bin/cat /etc/os-release 
NAME="Alpine Linux"
```

## PID namespaces

```sh
$ unshare --user --mount --root root --pid --fork --mount-proc /bin/sh                  
sh-5.2$ echo $$
1

~ $ /bin/ps aux
PID   USER     TIME  COMMAND
    1 nobody    0:00 /bin/sh
    3 nobody    0:00 /bin/ps aux

~ $ /bin/mount -v
proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
```

## Overlayfs

```sh
$ unshare --user --mount --root root --pid --fork --mount-proc --map-root /bin/sh

# mkdir /merged /work

# mount -t overlay overlay -o lowerdir=/bin,upperdir=/etc,workdir=/work /merged

# ls /merged
date
false
rc0.d
shells
...
```

## Applications

- Making tarballs with root-owned files (fakeroot)
- User-level chroot
- [Nix-user-chroot](https://github.com/nix-community/nix-user-chroot)
- Record/replay: [CARE](https://doi.org/10.1145/2618137.2618138)
- Network namespaces: virtual networks
- Sandboxes
  - Nix
  - [Bubblewrap](https://wiki.archlinux.org/title/Bubblewrap)
- Containers
  - [Creating containers from scratch](https://www.alanjohn.dev/blog/Deep-dive-into-Containerization-Creating-containers-from-scratch)

# cgroups

## Origins

- Olden days
  - global `/etc/security/limits.conf`
  - `getrusage(3)`

- "process control group"
  - [More info on LWN](https://lwn.net/Articles/604609/)

- > to organize processes hierarchically and distribute system resources along the hierarchy -[Linux Kernel Manual](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)

## cgroup controllers

- Types: weights, limits, protections, allocations
- CPU, memory, IO PIDs, cpuset, RDMA, HugeTLB

## cgroups API

- Completely file-oriented API for introspection
- Documentation [here](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html#interface-files)

```
$ cat /proc/$$/cgroup
0::/user.slice/user-1000.slice/user@1000.service/app.slice/emacs.service

$ cat /sys/fs/cgroup/user.slice/user-1000.slice/user@1000.service/app.slice/emacs.service/cgroup.procs
1234
45567

$ ps xawf -eo pid,user,cgroup,args | less
 478242 sam      0::/user.slice/user-1000.sl  \_ /run/current-system/sw/bin/podman
 478647 sam      0::/user.slice/user-1000.sl  \_ /nix/store/3bmd0vmvvvrashaxqb1d1apyy7smix3d-conmon-2.1.8/bin/conmon --api-version 1 -c 486d4b2bd61536c9eee04
478649 100000    0::/user.slice/user-1000.sl      \_ /nix/store/q8qq40xg2grfh9ry1d9x4g7lq4ra7n81-bash-5.2-p21/bin/sh /usr/bin/entrypoint --verbose --name sam
1085564 100000   0::/user.slice/user-1000.sl          \_ sleep 15
```

## cgroups API

```
$ ls /sys/fs/cgroup
cgroup.controllers
cgroup.stat
cpuset.mems.effective
io.cost.model
...

$ sudo mkdir /sys/fs/cgroup/test

$ ls /sys/fs/cgroup/test
cgroup.controllers
cgroup.stat
cpuset.mems.effective
io.cost.model
...

$ cat /proc/$$/cgroup
0::/user.slice/user-1000.slice/user@1000.service/app.slice/emacs.service

$ echo $$ | sudo tee /sys/fs/cgroup/test/cgroup.procs

$ cat /proc/$$/cgroup
0::/test

$ echo $$ | sudo tee 0::/user.slice/user-1000.slice/user@1000.service/app.slice/emacs.service/cgroup.procs

$ sudo rmdir /sys/fs/cgroup/test/user/root/0

$ sudo rmdir /sys/fs/cgroup/test/user/root

$ sudo rmdir /sys/fs/cgroup/test/user/

$ sudo rmdir /sys/fs/cgroup/test/
```

## cgroups can limit your mem

```xonsh
@ sudo mkdir /sys/fs/cgroup/test

@ echo @(os.getpid()) | sudo tee /sys/fs/cgroup/test/cgroup.procs
1122250

@ echo @(1024 * 1024) | sudo tee /sys/fs/cgroup/test/memory.max
1048576

@ for i in range(10, 30):
.......     print(f"Allocating {2**i}")
.......     x = len(b"_" * (2**i))
.......
Allocating 1024
Allocating 2048
Allocating 4096
Allocating 8192
Allocating 16384
Allocating 32768
Allocating 65536
Allocating 131072
Allocating 262144
Allocating 524288
Allocating 1048576
Allocating 2097152
Allocating 4194304
Allocating 8388608
Allocating 16777216
Allocating 33554432

Killed
```

## cgroups limiting forkbombs

```sh
$ echo 100 | sudo tee /sys/fs/test/pids.max
$ :(){ :|:& }; :  
:: fork failed: resource temporarily unavailable
```

## cgroups in your systemd

```
$ systemctl status
$ systemctl -t slice
$ systemd-run --scope -p MemoryMax=2G --user command
$ sudo systemctl set-property md5sum.service CPUShares=1024
```

## Applications

- Limit naughty apps
- Better accounting [BenchExec](https://github.com/sosy-lab/benchexec/)
- Docker/Podman/LXC

# Container ecosystem

## Container engines

- [systemd-nspawn](https://wiki.archlinux.org/title/Systemd-nspawn) (rootful)
- Docker (rootful daemon, going rootless)
- Podman (rootless)
- [Singularity](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0177459) (rootless or setuid)
- [CharlieCloud](https://dl.acm.org/doi/pdf/10.1145/3126908.3126925) (rootless)
- [Sysbox](https://github.com/nestybox/sysbox) (rootless)

## Container runtimes

- Container runtimes
  - CRI-O, containerd, runc, crun
    - [Source](https://www.tutorialworks.com/difference-docker-containerd-runc-crio-oci/)
  - CRI (Common Runtime Interface)

## Image formats

- OCI (Open Container Initiative)
- [Docker layers vs Nix](https://grahamc.com/blog/nix-and-layered-docker-images/)

```sh
$ let
  pkgs = import <nixpkgs> {};
in pkgs.dockerTools.buildLayeredImage {
  name = "my-image";
  tag = "latest";
  config.Cmd = [ "${pkgs.bashInteractive}/bin/bash" ];
  contents = [
    pkgs.pciutils
  ];
}

$ nix-build test.nix

$ docker load < result

$ docker run --rm -it localhost/my-image:latest
bash-5.2# ls
bash: ls: command not found
bash-5.2# lspci
00:00.0 Host bridge
00:02.0 VGA compatible controller
...

$ dive podman://localhost/my-image:latest

$ cp result result-old

$ edit test.nix to have a second package, also change tag

$ nix-build test.nix

$ docker load < result

$ diffoci diff --semantic podman://localhost/my-image:latest podman://localhost/my-image:latest2 | less --chop-long-lines
```

# Discussion

## Discussion

- Have OSes failed?
  - Processes were supposed to give us isolation.
  - Filesystem is already a hierarchical namespace.
  - Process groups already exist.

- > "Hypervisors are the living proof of operating system's incompetence" --[Glauber Costa](https://lwn.net/Articles/524952/)

## Discussion

- Systemd > SysV because of cgroups?

## Discussion

- Attack surface of namespaces?
- [What does enabling unprivileged usrns do?](https://security.stackexchange.com/questions/209529/what-does-enabling-kernel-unprivileged-userns-clone-do)

## Discussion

- Containers vs VMs for security, performance isolation?
- [Potential security risks](https://stackoverflow.com/questions/32257830/what-are-the-potential-security-problems-running-untrusted-code-in-a-docker-cont)
- [Docker as a sandbox for untrusted code](https://security.stackexchange.com/questions/107850/docker-as-a-sandbox-for-untrusted-code)
- [Bubblewrap](https://github.com/containers/bubblewrap)
  - Setuid implementation of a subset of user namespaces
  - ```sh
  bwrap \
      --ro-bind /usr /usr \
      --symlink usr/lib64 /lib64 \
      --proc /proc \
      --dev /dev \
      --unshare-pid \
      --new-session \
      bash
  ``` 

## Discussion

- Dis/advantages of the file API? vs ioctl?
- Nested virtualization still sucks

## Discussion

- Does it nest nicely?
- [Do not use docker-in-docker for CI](https://jpetazzo.github.io/2015/09/03/do-not-use-docker-in-docker-for-ci/)

## Discussion

- Episteme: scientific knowledge
- Techne: "how to" knowledge
- Doxa: common belief or popular opinion
- Phronesis: wisdom/prudence
