#define _GNU_SOURCE
#include <sys/syscall.h>

#define STDOUT 1

#define MSG_LEN 14
char msg[MSG_LEN] = "hello world\n";


__attribute__((force_align_arg_pointer))
void _start() {
    unsigned long ret;
    asm volatile
    (
        "syscall"
        : "=a" (ret)
        : "0"(SYS_write), "D" (STDOUT), "S" (msg), "d"(MSG_LEN)
        : "rcx", "r11", "memory"
    );

    asm volatile
    (
        "syscall"
        : "=a" (ret)
        : "0"(SYS_exit), "D" (0)
    );

	return 0;

	__builtin_unreachable();
}
