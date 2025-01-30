---
title: "Linux"
---

# Intro

<style>
.kinda-small {
  font-size: 80%;
}
.small {
  font-size: 40%;
}
.fragment.show-up {
  display: none;
}
.fragment.show-up.visible {
  display: inline;
}
.preserve-text {
  text-transform: none;
}
</style>

## How to compile

Compile me with:

```
pandoc --standalone --to=revealjs --output=README.html README.md --slide-level=2
```

Then open `README.html` in browser.

# what

##

[What you're refering to as Linux, is in fact, GNU/Linux, or as I've recently taken to calling it, GNU plus Linux.]{.fragment .strike}

[No, that's quite enough of that]{.fragment .show-up}

## Linux is a kernel

::::{.incremental}
[A kernel is a low-level piece of software that interfaces with the hardware and provides abstractions to higher level software.]{.fragment}

[Linux is a kernel based on the Portable Operating System Interface (POSIX).]{.fragment}
::::

## [...what does it *do* [(non-exhaustive)]{.small}]{.preserve-text}

::::{.incremental}
The kernel provides abstractions like

- virtual memory
- processes
- files

by implementing behavior like

- paging
- scheduling
- device drivers
::::

## Linux is a Operating System

::::{.incremental}
[What you're refering to as Linux, is...]{.fragment .strike .kinda-small} [*I said no!*]{.fragment .kinda-small} 

["Linux" also refers to Operating Systems based on the Linux kernel]{.fragment}

[These operating systems usually combine the Linux kernel with userland (not kernel) utilites like the GNU coreutils or busybox, as well as a compiler toolchain like gcc or clang.]{.fragment}
::::

## Linux is a community

::::{.incremental}
[That's us!]{.fragment}

[Linux and FOSS software and the people who develop them are all intertwined, while it can be intimidating, most of them are nice people!]{.fragment}
::::

# why

##

::::{.incremental}
[Everyone has a slightly different reason that *they* use linux, but many common points are:]{.fragment}

- free [as in freedom, free as in beer]{.fragment}
- customizable
- secure
::::

#

