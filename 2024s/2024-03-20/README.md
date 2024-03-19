---
title: "Package Managers"
---

Compile me with:

```
pandoc --standalone --to=revealjs --output=README.html README.md
```

---

## Definition

A package manager is a program that can install, update, and remove other programs

## Axes of differentiation

- Binary or from source
  - If from source: reproducible, locally optimized, or neither
  - If from source: binary cache or not
- Requires superuser or not
- Supports multiple environments or not
- Resolves dependency versions or single consistent version

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
