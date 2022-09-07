# Options for running Linux by Samuel Grayson

- [Popularity contest](https://forms.gle/F2goF2uT7Qp9kmaWA)

- Running Linux
  - Dual-booting
    - Partition hard-drive, select which partition to boot each restart
    - Can have shared partition between Windows and Linux
    - [guide](https://ubuntu.com/tutorials/install-ubuntu-desktop)
	  - We've already done steps 1 -- 3 for you.
    - Pros:
      - Best performance
      - Most feature-complete
    - Cons:
      - Have to partition harddrive, dangerous and less space for both
      - Be careful around the bootloader!
  
  - Windows Subsystem for Linux (WSL2)
    - Requires Windows 10 or newer
    - Syscall is how the application talks to the OS. MS adapted the NT kernel to implement some of Linux syscalls, so the Linux applications work fine in WSL.
    - Some tricky stuff is virutalized.
    - Is this Microsoft's last-ditch effort to prevent users from switching?
    - [Guide](https://docs.microsoft.com/en-us/windows/wsl/install)
    - (join Windows Insiders to get WSL 2)
    - Pros:
      - Easier to send files to/from Windows
      - Now has GPU support!
    - Cons:
      - Not feature complete (perf, Docker, Linux firewall, alternative filesystems (ZFS))
  
  - Virtual machine
    - Program that intercepts syscalls (normally would go straight to kernel) and executes them by proxy.
    - Docker on non-Linux requires virtualization.
    - For Windows, I suggest [Hyper-V](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/quick-create-virtual-machine).
    - For MacOS, I suggest [VirtualBox](https://www.howtogeek.com/657464/how-to-install-a-windows-10-virtualbox-vm-on-macos/). This guide is for Windows; replace with Ubuntu ISO.
    - Pros:
      - Guarantee of isolation
    - Cons:
      - Slower
      - Harder to use (meta key, etc.)

- Desktop environments
  - In Linux, the look-and-feel is totally customizable
  - Common desktop environments are: GNOME 3 (good for touch screens), KDE Plasma, Cinnamon (more like Windows XP), XFCE, LXDE (lightweight)

- Intermezzo: Installfest!
  - If you want to try Linux: we can help you with any of these options.
  - If you already have Linux:
    - Try installing and using a different desktop environment. Enlightment looks interesting.
    - Try installing another OS in a VirtualBox, QEMU, or Vagrant.
      - Redox is a next-generation Rust-based microkernel OS (everything is not a file; everything is a URL).
      - ReactOS is a clean-room reverse-engineered clone of Windows XP.
      - MirageOS and [Rumpkernel](https://github.com/rumpkernel/wiki/wiki/Tutorial%3A-Building-Rumprun-Unikernels) are unikernel compilers; they turn a single application into a bootable OS. Could be useful for making tiny containers or embedded systems with limited resources.
      - [Fuschia](https://fuchsia.dev/) is Google's next-generation OS, bringing back capability-based security and microkernel design into the modern era.
      - [Inferno](https://www.vitanuova.com/inferno/) is an open-source clone of Plan 9. It's the most UNIXy UNIX (everything is a file), migrate processes across machines, "union directory".

- Doing common tasks in Linux
  - Thunderbird (email)
    - https://answers.uillinois.edu/illinois/page.php?id=47659
  - Edit Microsoft documents
    - LibreOffice
    - WPS Office https://www.wps.com/office/linux/
  - Firefox, Chromium, or Google Chrome
