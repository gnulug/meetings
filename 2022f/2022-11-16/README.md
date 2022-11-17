
- Q: What format is compiled code in?
- A: [ELF format](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format)

![](https://upload.wikimedia.org/wikipedia/commons/e/e4/ELF_Executable_and_Linkable_Format_diagram_by_Ange_Albertini.png)

- Dynamic libraries (*.so), static libraries (*.a), object files (*.o), and executables (no extension)

  - *.c gets compiled to *.o, which gets archived to *.a (static library)
  - *.c gets compiled to *.o, which gets linked to * (executable), often the steps happen in one `gcc` command.
  - *.c gets compiled to *.so

- During linking, the linker figures out what address each function will be stored at. It turns function calls into jumps to those addresses.
- However, shared objects can't assume they will be loaded at any specific address; so they have to be written in [position independent code](https://en.wikipedia.org/wiki/Position-independent_code).

- ELF has a table saying what symbols the object file imports and what symbols it requires.

```
$ # Read the ELF symbol table
$ nm -D $(which ls)
                 U abort@GLIBC_2.2.5
                 U __assert_fail@GLIBC_2.2.5
...
$ # `U` means "undefined", so they are not defined in that binary; they have to be imported from another library.
$ ldd $(which ls)
        linux-vdso.so.1 (0x00007ffe2b9b4000)
        libselinux.so.1 => /lib/x86_64-linux-gnu/libselinux.so.1 (0x00007f10c0a13000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f10c07eb000)
        libpcre2-8.so.0 => /lib/x86_64-linux-gnu/libpcre2-8.so.0 (0x00007f10c0754000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f10c0a7e000)
$ # This shows us the libraries ls is requesting, and where they can be found on our system (using LD_LIBRARY_PATH).
$ LD_PRELOAD=/path/to/something.so ls
$ # this will import symbols from something.so
```

- The [loader](https://linux.die.net/man/8/ld-linux) is responsible for arranging everything in memory.
- The loader will load `LD_PRELOAD` shared objects ahead of others.
- We can use this to replace those from libc or whatever other library.
- Examples: https://github.com/gaul/awesome-ld-preload/blob/master/README.md
  - libfaketime: make calls to the current time return a fake time
    - `FAKETIME="2020-01-01 00:00:00" LD_PRELOAD=/usr/lib/x86_64-linux-gnu/faketime/libfaketime.so.1 python -c 'import time; print(time.ctime())'`
  - libeatmydata: make `fsync()` a no-op (very dangerous!)
  - libleakmydata: accept all SSL certificates.
  - http://zlibc.linux.lu/install.html

- Our program:

```
$ cat test.c
#define _GNU_SOURCE

#include <stdint.h>
#include <stddef.h>
#include <stdio.h>
#include <unistd.h>
#include <dlfcn.h>

ssize_t getrandom(void *buf, size_t buflen, unsigned int flags) {
    // Full buf with buflen bytes of deterministic random data
    for (size_t i = 0; i < buflen; ++i) {
        ((char*)buf)[i] = 42;
    }
    return buflen;
}

$ gcc -fPIC -shared -o test.so test.c
$ python -c 'import random; print(random.randint(0, 99))'
28
$ python -c 'import random; print(random.randint(0, 99))'
73
$ python -c 'import random; print(random.randint(0, 99))'
23
$ LD_PRELOAD=./test.so python -c 'import random; print(random.randint(0, 99))'
6
$ LD_PRELOAD=./test.so python -c 'import random; print(random.randint(0, 99))'
6
$ LD_PRELOAD=./test.so python -c 'import random; print(random.randint(0, 99))'
6
```
