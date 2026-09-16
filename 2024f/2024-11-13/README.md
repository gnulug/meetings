# Sam's research

- [Sam's prelim (motivation)](https://github.com/charmoniumQ/thesis/blob/main/prelim_pres/main.html)
- [Library interposition (`LD_PRELOAD`) GLUG presentation](https://github.com/gnulug/meetings/tree/master/2022f/2022-11-16)
- [Address-space layout randomization is not as good as you think](https://arxiv.org/pdf/2408.15107)
- [setarch](https://www.man7.org/linux/man-pages/man8/setarch.8.html) and [personality](https://www.man7.org/linux/man-pages/man2/personality.2.html)
- [Snakemake Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC8114187/)
- [Reinhart-Rogoff Excel spreadsheet error](https://theconversation.com/the-reinhart-rogoff-error-or-how-not-to-excel-at-economics-13646)
- [Zpoline (replacing syscall with funccall)](https://www.usenix.org/system/files/atc23-yasukata.pdf)
  - [Zpoline GitHub](https://github.com/yasukata/zpoline)
  - ptrace is too slow for your project.
  - the LD_PRELOAD trick is not enough because it cannot exhaustively hook system calls.
  - you cannot anticipate the availability of the source code of your hook target.
  - you do not want to modify the OS kernel or install a kernel module.
  - Also see a similar project, [SaBRe paper](https://link.springer.com/article/10.1007/s10009-021-00644-w) [SaBRe GitHub](https://github.com/srg-imperial/SaBRe)
- [Slotted pages](https://siemens.blog/posts/database-page-layout/)

