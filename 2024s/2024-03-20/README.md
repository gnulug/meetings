---
title: "Package Managers"
---

##

Compile me with:

```
pandoc --standalone --to=revealjs --output=README.html README.md
```

Or view [here](https://htmlpreview.github.io/?https://github.com/gnulug/meetings/blob/master/2024s/2024-03-20/README.html)

## Objectives

- Why are there so many package managers?
- How do their design choices differ?
- Take only 20 mins

## Definition

A package manager is a program that can install, update, and remove other programs. Installation should also install the program's dependencies at compatible versions.

- Excludes dpkg/RPM in favor of APT/YUM
- Excludes frontends (Aptitude, ...)
- Excludes XStow/GNU Stow

## Major axes of differentiation

- Binary or from source
- Requires privilege or not
- Dependency solver (multiple installable versions) or not

##

<style>
#sams-matrix {
  font-size: 4vh;
}
</style>
<table id="sams-matrix">
<thead>
<tr><th>Source?</th><th>Unpriv?</th><th>Dep solv?</th><th>Examples</th></tr>
</thead>
<tbody>
<tr><td>N</td><td>N</td><td>N</td><td>Distro pkg mgrs (XBPS, Pacman)</td></tr>
<tr><td>N</td><td>N</td><td>Y</td><td>Distro pkg mgrs (APT, DNF, APK)</td></tr>
<tr><td>N</td><td>Y</td><td>N</td><td></td></tr>
<tr><td>N</td><td>Y</td><td>Y</td><td>Conda</td></tr>
<tr><td>Y</td><td>N</td><td>N</td><td></td></tr>
<tr><td>Y</td><td>N</td><td>Y</td><td></td></tr>
<tr><td>Y</td><td>Y</td><td>N</td><td>Ports-inspired (pkgsrc, Portage, MacPorts, Home/Linuxbrew), Functional pkg mgrs (Nix, Guix)</td></tr>
<tr><td>Y</td><td>Y</td><td>Y</td><td>Spack, 0install, $lang-level</td></tr>
</tbody>
</table>

## Caveats

- Based on how they are used not theoretical capabilities.

- If install build-deps and invoke compiler is not automatic, it's not build-from-source
  - e.g., I call APT "not from source" even though apt-source exists

- [Gentoo Prefix on other OSes](https://wiki.gentoo.org/wiki/Project:Prefix/Use_cases)

- [0install comparison matrix](https://docs.0install.net/about/comparison/)

## Binary vs source

- Binary: faster, requires centralized repo
- Centralized repos are expensive, get purged, require trust
- ```Dockerfile
  FROM debian:stretch
  RUN apt-get update
  # hangs forever after 2024 :)
  ```
- From-source with binary cache is almost as fast
  - Public cache or site-wide cache

## Privilege vs unprivileged

- Priv: Write pkgs to `/bin` ([Filesystem Standard](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html))
  - Share packages between users
  - Makes sense when disk space was expensive; Now its hard to change
- Unpriv: Write pkgs to `$PREFIX` & add to `$PATH`
  - Principle of least privilege
  - Allows multiple envs
  - Optional privileged daemon, still share packages between users

## Dependency solving: Diamonds

<img src="https://learn.microsoft.com/en-us/dotnet/standard/library-guidance/media/dependencies/diamond-dependency.png" alt="App deps on Web lib; App deps on Logging lib; Web lib deps on JSON lib &gt;=1.0; Logging lib deps on JSON &gt;= 2.0" />

## Dependency solving is NP-complete

- Solving dep versions is NP-complete. [Proof](https://research.swtch.com/version-sat)
  - Some algos using SAT-solvers ([1](https://hal.science/hal-00149566/document) [2](https://ieeexplore.ieee.org/abstract/document/4222580) [3](https://docs.0install.net/developers/solver/) [4](https://github.com/openSUSE/libsolv))
- After 2020, Pip uses SAT solve
- Slowest part of conda is often solving!
- [APT can solve sudoku](https://web.archive.org/web/20160329115022/http://algebraicthunk.net/~dburrows/blog/entry/package-management-sudoku/)

## Avoid dep solves: 1 version

- [Golden Rule: globally coherent versions](https://www.haskellforall.com/2022/05/the-golden-rule-of-software.html)
  - E.g., [Stackage](https://www.fpcomplete.com/blog/stackage-server/), globally coherent set of Hackage packages (Haskell)
- Distro pkg mgrs (APT, DNF) and functional pkg mgrs (Nix, Guix) get on fine
- Volunteer developers maintaining more than one release? Hard

## Avoid dep solves: Semver

- Semver dictates same major-version, at least greater bugfix/patch >=3.7.1,<4
- Don't know when breaking compatibility ([Hyrum's law](https://www.hyrumslaw.com/))
  - E.g., [1](https://github.com/pyca/cryptography/issues/5771#issuecomment-775990406), [2](https://github.com/ipython/ipython/issues/12740), [3 ](https://twitter.com/brettsky/status/1262077534797041665) , 

## 

<a href="https://xkcd.com/1172/">
<img src="https://imgs.xkcd.com/comics/workflow_2x.png" alt="There are probably children out there holding down spacebar to stay warm in the winter! YOUR UPDATE MURDERS CHILDREN. (copied image and alt from XKCD)"/>
</a>

<!--
## $Lang package managers

- Library development vs application deployment
  - Spec file vs lock file
  - Known to be compatible vs known to be incompatible
- Are version caps bad?
  - [Should Stackage ignore version bounds?](https://www.stackage.org/blog/2018/01/ignore-version-bounds)
  - [Lenient lower bounds](https://www.fpcomplete.com/blog/lenient-lower-bounds/)
  - [Never version cap](https://iscinumpy.dev/post/bound-version-constraints/#tldr)
-->

## Avoid dep solves: Private deps

- "Private" deps
  - No types or fns in public interface (or split into two libraries) and no globals
- [Why does this not cause problems in JS?](https://stackoverflow.com/questions/25268545/why-does-npms-policy-of-duplicated-dependencies-work)
- [NPM deps vs peer-deps; can other languages?](https://lexi-lambda.github.io/blog/2016/08/24/understanding-the-npm-dependency-model/)
- [npm dedupe](https://docs.npmjs.com/cli/v10/commands/npm-dedupe)
- [Can Haskell do that too](https://www.reddit.com/r/haskell/comments/4zc6y3/comment/d6vkm62/)
- Could deps be classified pub/priv with static analysis?

## Bootstrapping

- Nix, Spack: prerequisites including C compiler [Nix](https://nixos.org/manual/nix/stable/installation/prerequisites-source) and [Spack](https://spack.readthedocs.io/en/latest/getting_started.html)
- [Reflections on Trusting Trust](https://dl.acm.org/doi/abs/10.1145/358198.358210)
- [Guix full-source bootstrap](https://guix.gnu.org/en/blog/2023/the-full-source-bootstrap-building-from-source-all-the-way-down/)

## $lang pkg mgrs

- Examples: Pip, Cargo, NPM, Yarn, RubyGems, CPAN, Stack, Cabal, opam, Maven, SBT, tlmgr
- Supports multiple environments (usually)
- Downloads/builds source (usually)
- Privs only required for global env (usually)
- Shoddy support for native code (usually)
- Has dep solver (usually)

## Spack

## Requirements for HPC systems

- Manage extremely complex package dependencies
  - Need multiple versions of the same package installed at once
- Automate the build process of packages
- Install multiple complex pieces of software at once
  - Cope with combinatorial versioning

##

![](ARES-dependencies.png)

## Spack's Key Innovations

- Composable package descriptions
  - Packages are described parametrically
  - Same idea as templates in C++ or generics in Rust
- Spec syntax for specifying depedency graphs and constraints
- A concretization process to stamp out a concrete build specification

## Package descriptions

- Embedded DSL inside Python
- Parameterized via the `spec` argument of the `install` method

![](SpackPackage.png)

## Spack Specs

- Specification on an install supplied after `spack install`
  - Small enough usually to be a command line parameter
  
##

![](Specs.png)

##

![](MoreSpecs.png)
![](SpecsInDependsOn.png)

## Concretization

1. Spack intersects the DAG from the user's specs and another DAG created from directives in the package files
  - There may be conflicts if the user inadvertedly requests two versions of the same package, for example

## Concretization

2. Resolve virtual dependencies into normal dependencies
  - Select a particular implementation of MPI, BLAS, etc.

## Concretization

3. Greedily select concrete versions of packages until entire DAG is concrete
  - NOTE: this is all from their 2015 paper - "We leave automatic constraint space exploration for future work."

##

![](ConcreteAlgo.png)
![](ConcreteExample.png)

## Concretization Today

- Uses a logic solver to support full backtracing and optimization
  - Called `clingo`
- Written using Prolog

## Concretization Today

- Unfortunately, there isn't much public writing about `clingo`
- Gist: express constraints on concrete spec based on abstract DAG
- Dispatch logic solver (Prolog) to solve all of the constraints
- NP-complete, but fast in practice
