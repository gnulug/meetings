# Package managers

|                           | Apt/Dnf/PM | Portage/Ports/... | Nix/Guix | AppImage | Flatpak | Docker/Podman |
|---------------------------+------------+-------------------+----------+----------+---------+---------------|
| Reproducible builds       | No (guess) | No (guess)        | Yes!     | N/A      | N/A     | N/A           |
| Is it fast?               | mid        | fast if $$$       | Fast     | Fast     | Fast    | Can be        |
| Ecosystem completeness?   | YMMV       | Better maybe?     | Good     | Bad      | Good    | Good          |
| Ecosystem up-to-dateness? | YMMV       | Better maybe?     | Good     | Ok?      | Good    | Good          |
| Multiple simul versions   | No         |                   | Yes!     |          |         |               |
|                           |            |                   |          |          |         |               |


-  Questions
  - How does this package manager work?
  - How is this different from other package managers?
  - Does this package manager duplicate common dependencies?
  - Does this package manger support multiple versions on the same machine?
  - Can this package manger package system services?
  - Can this package manger package system kernel modules?
  - Does this package manger have a centralized repository?
  - Does this package manager build from source?
    - If from source, how long does it take to compile Rust? ;P
  - How many up-to-date packages in Repology?
  - Is easy to use?
  - Is easy to write new packages?
  - https://github.com/AppImage/AppImageKit/wiki/Similar-projects#Comparison
- More links
  - https://www.reddit.com/r/linux/comments/4ohvur/comment/d4d7h05/?utm_source=share&utm_medium=web2x&context=3
    - Nix/Guix solves every single problem that Flatpak and Snappy claim to solve in a much, much more elegant and better way except for one thing: Allowing proprietary software developers to more easily distribute. (Or rather software developers whose source code is not public, you can have public source proprietary software.)
  - http://0pointer.net/blog/revisiting-how-we-put-together-linux-systems.html
  - https://www.reddit.com/r/linux/comments/2f4oe7/comment/ck65ska/
  - https://ludocode.com/blog/flatpak-is-not-the-future
  - https://news.ycombinator.com/item?id=29316024
    - Fedora publishes its Flatpak of GIMP as org.gimp.GIMP. This conflicts with the official org.gimp.GIMP published by the GIMP developers on Flathub.
