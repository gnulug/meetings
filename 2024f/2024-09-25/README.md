---
title: "The Nix™ Way of Life"
---

# Intro

<style>
.kinda-small {
  font-size: 80%;
}
</style>

## How to compile

Compile me with:

```
pandoc --standalone --to=revealjs --output=README.html README.md --slide-level=2
```

Then open `README.html` in browser.

## Objectives

<style>
  .fragment.show-up {
    display: none;
  }
  .fragment.show-up.visible {
    display: inline;
  }
</style>

:::: {.incremental}

- [What is]{.fragment .strike} [Why invent]{.fragment .show-up} Nix pkg manager?
- [What is]{.fragment .strike} [Why invent]{.fragment .show-up} NixOS?
- How to use Nix pkg manager → standard dev env? **Not NixOS**
- How to use Nix home-manager → dotfiles? **Not NixOS**
- How to use NixOS → roll-backable systems? **Yes NixOS**

::::

## Jargon note

:::: {.kinda-small .incremental}

- Nix language
  - Manual: <https://nixos.org/manual/nixos/stable>
  - Quick ref: <https://learnxinyminutes.com/docs/nix/>
- Nix package manager: use nix lang to define package recipes
  - Manual: <https://nix.dev/manual/nix/2.18/>
- NixOS: uses nix pkg mgr and nix lang
  - Manual: <https://nixos.org/manual/nixos/stable>
- Nixpkgs repo: a set of recipes for nix pkg mgr
  - Manual: <https://nixos.org/manual/nixpkgs/stable/>
- Home-manager (third-party)
  - Manual: <https://nix-community.github.io/home-manager/>

::::

# Nix pkg manager

## Why have root package managers?

:::: {.incremental}

- Poll: Do you use root to install packages (e.g., new Firefox)?
- Unix FHS, "everything just works" [lmao]{.fragment}
- Disk-space is expensive
- Building packages is hard

::::

## Root-less package managers

<style>
#pkg-mgr-matrix {
  font-size: 4vh;
}
.highlight {
  color: #A0FFA0;
}
</style>
<table id="pkg-mgr-matrix">
<thead>
<tr><th>Source?</th><th>Unpriv?</th><th>Dep solv?</th><th>Examples</th></tr>
</thead>
<tbody>
<tr><td>N</td><td>N</td><td>N</td><td>Distro pkg mgrs (XBPS, Pacman)</td></tr>
<tr><td>N</td><td>N</td><td>Y</td><td>Distro pkg mgrs (APT, DNF, APK)</td></tr>
<tr class="highlight"><td>N</td><td>Y</td><td>N</td><td></td></tr>
<tr class="highlight"><td>N</td><td>Y</td><td>Y</td><td>Conda</td></tr>
<tr><td>Y</td><td>N</td><td>N</td><td></td></tr>
<tr><td>Y</td><td>N</td><td>Y</td><td></td></tr>
<tr class="highlight"><td>Y</td><td>Y</td><td>N</td><td>Ports-inspired (pkgsrc, Portage, MacPorts, Home/Linuxbrew), Functional pkg mgrs (Nix, Guix)</td></tr>
<tr class="highlight"><td>Y</td><td>Y</td><td>Y</td><td>Spack, 0install, $lang-level</td></tr>
</tbody>
</table>

## Advantages of root-less

:::: {.incremental}
- Can simply manipulate `$PATH`, `$PYTHON_PATH`, `$CLASSPATH` to make packages appear to be installed/uninstalled
  - Must load something in shell: `source ./activate.sh` or `nix develop`
- Each user can install their own pkgs
- Better security, principle of least privilege
- Root-less → multiple environments (project-specific)
- Private dependencies (wrapper scripts)
::::

## Purity and cache

<style>
.small {
  font-size: 3vh;
}
</style>

:::: {.incremental}

- Nix code is pure
- Build scripts run in sandbox (aka "hermetic" [Spradlin and Lodato 2020 (Google) ](https://google.github.io/building-secure-and-reliable-systems/raw/ch14.html))
- Much like [Pants](https://www.pantsbuild.org/), [Buck2](https://buck2.build/), [Bazel](https://bazel.build/), etc.
- Cache (aka "nix store"): hash-of-inputs (Nix src + pkgs src) to files or directories
  - [`/nix/store/0a0khkw34v25q8k6p44ma1rqa479r1za-gnutar-1.35/`]{.small}
  - [Has `.../bin/tar` and `.../share/man/man1/tar.1.gz`]{.small}
- Used whenever the hash matches (purity)
- Can be shared with other users and remote

::::

## Other comparisons

:::: {.incremental}

- Nix vs Pip/Virtualenv:

  - Both can create virtual environments
  - Nix can manage non-Python package (e.g., Ruff, pandoc, etc.)

- Nix vs Conda:

  :::: {.nonincremental}
  - Conda uses bins; Nix uses source with bin cache
  - Equally fast for common (cached) packages
  - From-source is more flexible and reliable
  ::::

::::

## Other comparisons

- Nix vs Spack:
  - [The Spack Package Manager (Gamblin et al. 2015)](https://dl.acm.org/doi/abs/10.2807623/1145.2807591)
  - Spack does SAT-solve: `spack install python@3.12.4 py-requests@3.5.6`
  - Nix has globally-consistent package set: `nix-env -i python pythonPackages.requests`
    - Select older revision of package set to get older versions
    - <https://lazamar.co.uk/nix-versions/>
  - Nix has better hermeticity and cache

## Other comparisons

- Nix vs Guix:
  - See [Courtès 2013](https://arxiv.org/abs/1305.4584)
  - Same idea
  - Nix lang + Bash vs Guile Scheme (Lisp)

# Nixpkgs, *the* package repository

---

![](https://repology.org/graph/map_repo_size_fresh.svg?xlimit=40000&ylimit=20000)

---

![](https://repology.org/graph/map_repo_size_fresh.svg)

## Repology.org

- Nixpkgs unstable and latest Nixpkgs stable takes the cake for N packages and N up-to-date packages
- Excluding $language package managers, they also win % up-to-date packages
- <https://repology.org/repositories/statistics/pvulnerable>
- N maintainers?

# NixOS

---

![](https://pm1.aminoapps.com/6410/5987479a055e4f5cae60dff1581608840f365b9b_hq.jpg)

Do you have a moment to talk about our lord and savior, NixOS?

## Imperative vs declarative

:::: {.incremental .kinda-small}

- Imperative configuration

  :::: {.nonincremental}
  - Machine has mutable state (files on disk)
  - Run commands to change
  ::::

- Declarative configuration

  :::: {.nonincremental}
  - [NixOS: A purely functional linux distribution (Dolstra and Löh 2008)](https://dl.acm.org/doi/abs/10.1145/1411204.1411255)
  - Program that generates immutable state (r.o. files on disk)
  - Edit/re-execute program to change
  - In practice, shunt what can't be declarative into islands of imperativeness
  - Impermanence
  ::::

:::

## Imperative + Configuration manager

- "If ... the playbook description of a system and the actual system state don't agree, then Ansible will make whatever changes are necessary for the system to match the playbook."
  -- [Learning Ansible basics by RedHat](https://www.redhat.com/en/topics/automation/learning-ansible-tutorial)

- Imperative + Ansible/Chef/Puppet == Declarative?

- In my opinion, Imperative + Ansible/Chef/Puppet == sort of declarative, when things go right

## Declarative vs imperative

Declarative is:

:::: {.incremental}

- ✅ Roll-backable (c.f. btrfs snapshots)
- ✅ Reproducible
- ✅ State is predictable
- ✅ Cachable
- ❌ Sometimes slow
- ❌ Harder to use

::::

# Using Nix pkg manager for dev env

## Pros

- Manage packages in any language with the same package manager
- Have the exact same dev env on every system (Linux, MacOS, WSL)
- Cache makes CI go brrr

## Cons

- People have to install Nix to have your dev env
- Have to learn how to write Nix (small bit)
- Don't have as wide choices available for package versions

## Setup

:::: {.kinda-small}

- Don't already have Nix pkg manager? Follow [Determinate Systems installer](https://install.determinate.systems/)

- Already have Nix pkg manager? Make sure flakes are enabled `nix flake --help`

  - If not NixOS, [`echo "experimental-features = nix-command flakes" >> ~/.config/nix.conf`]{.small}

  - If NixOS, add [`nix.settings.experimental-features = [ "nix-command" "flakes" ];`]{.small} to your configuration
- No git or `git add -A`

::::

## First Flake

```sh
nix flake --template github:numtide/flake-utils
```

```nix
let
  pkgs = nixpkgs.legacyPackages.${system};
  python = pkgs.python312;
  requirements = pypkgs: [ pkgs.panflute ];
in
{
  devShells.default = pkgs.mkShell {
    packages = [
      (python.withPackages requirements)
      pkgs.ruff
      pkgs.pandoc
    ];
  };
}
```

## Usage instructions

- `nix develop`
- `nix develop --command zsh`
- direnv

## Apps and Docker images

- Apps
- Docker images
- <https://github.com/uiuc-cs527-fa24/mp2-validator>

## Garbage collection

- Simply remove pkg from flake.nix, no "uninstall step"
- Could be in use by others
- Solution: Take out the garbage
  - Delete everything in the store not reachable from a gc-root

# Using Nix home-manager for dotfiles

## Pros

- Dotfiles can come with packages/dependencies
- Dotfiles can be generated programatically

## Cons

- Have to install Nix to deploy your dotfiles
- Have to learn how to write Nix (small bit)

## Setup

- See setup of Nix pkg mgr with flakes from previous
- [Home-manager manual > Nix Flakes](https://nix-community.github.io/home-manager/index.xhtml#ch-nix-flakes)

## Writing the config

- [Home-manager options](https://nix-community.github.io/home-manager/options.xhtml)
- Firefox with settings
- zsh with starship
- Examine `~/.zshrc`
- Desktop bg image (adding options)
- [Sam's dotfiles](https://github.com/charmoniumQ/dotfiles.nix)

# Using NixOS

## Pros

- Roll-backable/reproducible state (at boot-time!)
- Use variables across your configs and machines
- First class support for ZFS
- Impermanence 

## Cons

- The learning curve is a shear cliff
  - Have to learn functional programming to upgrade Firefox
  - "infinite recursion encountered"
- In order for a program to run on NixOS it must be built or patched by nix
  - Proprietary software can be difficult
  - If it's not in nixpkgs, then you may have to write a derivation for it yourself

## home-manager integration

<style>
  code {
    background: #000000;
  }
</style>

```nix
programs.nushell = {
  enable = true;
  configFile.source = ../config/nushell/config.nu;
  envFile.source = ../config/nushell/env.nu;
  shellAliases = 
    lib.attrsets.filterAttrs
    (name: val: val != null)
    osConfig.environment.shellAliases;
    # ^ home-manager config is using 
    # information from system-wide config
};
```

---
