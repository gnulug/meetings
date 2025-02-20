---
title: "Linux SysRq Features"
---

# System Request: Introduction/History

- BIOS software interrupt → signals OS to invoke low-level functions
- Old software often bypassed the OS for keyboard input, so SysRq was used as a special key for switching between operating systems.
- Introduced with the IBM PC family in the mid-1980s
- Originally given a dedicated key
	- Later, moved to <kbd>Alt</kbd> + <kbd>Print Screen</kbd>
	- Today, many keyboards don't provide the function at all.
	- However, we will provide a quick demo on how to enable SysRq on an arbitrary keyboard.
- Used today for debugging purposes
	- Example: Linux's "magic SysRq key"
- Commonly abbreviated "SysRq" or "Sys Req"

# Configuration

- Enable by building kernel with `CONFIG_MAGIC_SYSRQ` set.
- `/proc/sys/kernel/sysrq` bitmask (read/write) for keyboard activation
	- 0: disable all SysRq functions
	- 1: enable all SysRq functions
	- 0x2: enable control of console logging level
	- 0x4: enable control of keyboard (SAK, unraw)
	- 0x8: enable debugging dumps of processes etc.
	- 0x10: enable sync command
	- 0x20: enable remount read-only
	- 0x40: enable signalling of processes (term, kill, oom-kill)
	- 0x80: allow reboot/poweroff
	- 0x100: allow nicing of all RT tasks

# Usage

Either:

- Press <kbd>Alt</kbd> + <kbd>SysRq</kbd> + [command key]
	- "Fn" might be needed on some keyboards or laptops
	- Check your laptop's documentation for other possible key combinations (e.g., <kbd>Fn</kbd> + <kbd>s</kbd>)
	- ChromeBooks: <kbd>Alt</kbd> + <kbd>Volume Up (F10)</kbd> + [command key]
- Write [command key] to `/proc/sysrq-trigger`

# How does it work?

When writing a driver for a UART serial device, code authors include `serial_core.h` to have their driver interface with the operating system.

The `serial_core.h` file directly calls SysRq functionality from `sysrq.c`. As a result, SysRq-related functions are implemented directly into these drivers, and drivers can call `uart_handle_sysrq_char()` and therefore run debugging or system recovery operations at link-level. 

USB seems to also have this functionality, implemented in a somewhat similar way.

More can be read here:

- <https://www.kernel.org/doc/Documentation/serial/driver>
- <https://github.com/torvalds/linux/blob/master/drivers/tty/sysrq.c>
- <https://github.com/torvalds/linux/blob/6537cfb395f352782918d8ee7b7f10ba2cc3cbf2/include/linux/serial_core.h#L1170>
- <https://github.com/torvalds/linux/blob/6537cfb395f352782918d8ee7b7f10ba2cc3cbf2/drivers/usb/serial/generic.c#L574>

# Command keys

When invoking functions with the keyboard, these command mappings assume a QWERTY layout.

|Command|Function                                                                                                                                                                                             |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|b      |Immediately reboot the system without syncing or unmounting disks.                                                                                                                                   |
|c      |Perform a system crash. A crashdump will be taken if configured.                                                                                                                                     |
|d      |Show all locks that are held.                                                                                                                                                                        |
|e      |Send a SIGTERM to all processes except init.                                                                                                                                                         |
|f      |Call the OOM killer to kill a memory-hog process, but do not panic if nothing can be killed.                                                                                                         |
|g      |Used by kgdb (kernel debugger)                                                                                                                                                                       |
|h      |Display SysRq cheatsheet help message. (Any key not listed in this table will also display help.)                                                                                                    |
|i      |Send a SIGKILL to all processes except init.                                                                                                                                                         |
|j      |Forcibly “Just thaw it” - filesystems frozen by the FIFREEZE ioctl.                                                                                                                                  |
|k      |Secure Access Key (SAK): Kill all programs on the current virtual console.                                                                                                                           |
|l      |Show a stack backtrace for all active CPUs.                                                                                                                                                          |
|m      |Dump current memory info to the console.                                                                                                                                                             |
|n      |Make RT tasks nice-able.                                                                                                                                                                             |
|o      |Shut the system off.                                                                                                                                                                                 |
|p      |Dump the current registers and flags to the console.                                                                                                                                                 |
|q      |Dump per-CPU lists of all armed hrtimers (but *not* regular timer_list timers) and detailed information about all clockevent devices.                                                                |
|r      |Turn off keyboard raw mode and set it to XLATE.                                                                                                                                                      |
|R      |Replay the kernel log messages on consoles.                                                                                                                                                          |
|s      |Attempt to sync all mounted filesystems.                                                                                                                                                             |
|t      |Dump a list of current tasks and their information to the console.                                                                                                                                   |
|u      |Attempt to remount all mounted filesystems read-only.                                                                                                                                                |
|v      |Forcefully restore framebuffer console.                                                                                                                                                              |
|w      |Dump tasks that are in uninterruptible (blocked) state.                                                                                                                                              |
|x      |(Not used on x86/x86_64)                                                                                                                                                                             |
|z      |Dump the ftrace buffer.                                                                                                                                                                              |
|0-9    |Sets the console log level, controlling which kernel messages will be printed to the console. (For example, 0 means that only emergency messages like PANICs or OOPSes would make it to the console.)|

# How do I use SysRq without a dedicated SysRq Key?

- First, set your SysRq permissions. This can be done either through `proc` or `sysctl`.
- Often, the easiest way to get immediate feedback is by entering a TTY. Enter a TTY (this can often be done by a combination of modifier keys and your Function keys) and go into a root shell. Enter `echo h > /proc/sysrq-trigger`, which should output the help menu.
- You often use SysRq when something is wrong with your userland, though. Having a key is useful.
- Manufacturers often use an alternative key combination for SysRq functionality. Check with your manufacturer on those details. Alternatively, you can implement the scancode-keycode mapping yourself. We will do it now on a Systemd Debian install using `evtest` and `udev`. `evtest` binaries are available in most package repositories. There are forks of `udev`, like `eudev` that establish the same functionality on non-Systemd systems.
- First, run `evtest` without any options. It will give you a list of character devices. Pick your keyboard, which is hopefully easy to identify. Keep its event id in mind.
- When you run `evtest`, each key press and release is associated with a scancode. Enter your key combination that you want to be SysRq. Remember that any time you hit <kbd>Alt</kbd> + [your keys] you will be running invasive commands, so ensure that it's not something you can fat finger easily.
- Recall that event id from before. If you run `cat /sys/class/input/event<number>/device/modalias`, you can obtain a brief view of the `sysfs` kernel identifier for your device. Laptop keyboards aren't going anywhere, but this functionality is useful for a usb keyboard.
- Now that we have this information, we can use `hwdb`. Go to `/etc/udev/hwdb.d/` and create a new file. For example, the demo can be `90-keyboard.hwdb`.
- Paste that `modalias` identifier you got from before. On the next line, enter a single space and write the line: `KEYBOARD_KEY_<your scancode>=sysrq`.
- Run `systemd-hwdb update; udevadm trigger` as root to load your new key-value pairs and update your device rules.
- Switch to TTY and enter <kbd>Alt</kbd> + [your keys] + <kbd>h</kbd>. If you see the same help menu, you did it!
- For some reason, I don't know why this information doesn't appear under `udevadm info` for the device.

# Resources

- <https://docs.kernel.org/admin-guide/sysrq.html>
- <https://en.wikipedia.org/wiki/Magic_SysRq_key>
- <https://en.wikipedia.org/wiki/System_request>
- <https://www.kernel.org/doc/Documentation/serial/driver>
- <https://github.com/torvalds/linux/blob/master/drivers/tty/sysrq.c>
- <https://github.com/torvalds/linux/blob/6537cfb395f352782918d8ee7b7f10ba2cc3cbf2/include/linux/serial_core.h#L1170>
- <https://github.com/torvalds/linux/blob/6537cfb395f352782918d8ee7b7f10ba2cc3cbf2/drivers/usb/serial/generic.c#L574>
