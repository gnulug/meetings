- [Build Systems à la Carte](https://www.microsoft.com/en-us/research/uploads/prod/2018/03/build-systems.pdf)
  - Scheduler Types
    - Topological: do a topological sort, and requires dependencies to be static. Easiest to parallelize.
    - Restarting: when a task requires some uncomputed dependency, stop it, do the dependency, and restart it. Best suited to dynamic dependencies. Parallelizing might do extra work, because threads might discover the same dependency.
    - Suspending: like restarting, but suspend task instead of stopping it (requires system support)
  - Determining out-of-date keys:
    - Dirty bit: Note that file mtime acts just like a dirty bit
    - Verifying trace: hash of immediate inputs
    - Constructive trace: hash of immediate inputs and output (for supporting early cutoff)
    - Deep constructive trace: hash of transitive inputs
  - Dependencies: static or dynamic
  - Minimal: only rebuild what is necessary
  - Cutoff: If compile(a) and compile(a-modified) are the same, and we already stored link(compile(a), ...), then link(compile(a-modified), ...) does not need to be re-comptued. For example, a and a-modified only changes the comments. This is an obvious optimization, but systems that use modification time, like Make, won't be able to do this.
  - Cloud: Can dispatch jobs to the cloud; we know what jobs to run ahead of time.
  - | Build System | Persistent Build Information | Scheduler | DeterminingOut-of-date keys | Dependencies | Minimal | Cutoff | Cloud |
    | Make |  | Topological | Dirty bit | Static | Yes | No | No
    | MS Excel | Order of last exec | Dirty bit | Restarting | Dynamic | No | No | No |
    | [Shake](https://shakebuild.com/) | Previous dep graph | Suspending | Verifying trace | Dynamic | Yes | Yes | No |
    | [Bazel](https://bazel.build/) | Cloud cache, commnad hist | Restarting | Constructive trace | Dynamic | No | Yes | Yes |
  - Other build systems
    - CloudBuild
    - Cloud Shake
    - Buck
    - Nix
    - Dune
    - Ninja
    - Ekam: make, but backwards (restarting, dynamic deps, dirty bit)
    - Pluto
    - Tup
    - Redo
    - Fabricate.py
