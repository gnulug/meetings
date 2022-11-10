#define A_COOL_SELF_COMPILING_PROGRAM /*

gcc -Wall $0 -o $(basename -s .c $0).exe
exec ./$(basename -s .c $0).exe "$@"
Bash doesn't get past the previous line
*/

#include <sys/types.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
#include <stdio.h>

#define BUFFER_SIZE 1024
char buffer[BUFFER_SIZE];

int main(int argc, char** argv) {
	int in_fd = open(argv[1], O_RDONLY);
	if (in_fd < 0) {
		perror("open");
		exit(1);
	}

	int out_fd = open(argv[2], O_WRONLY | O_TRUNC | O_CREAT, 0644);
	if (out_fd < 0) {
		perror("open");
		exit(1);
	}

	size_t total_bytes_read = 0;
	while (1) {
		size_t bytes_read = read(in_fd, buffer, BUFFER_SIZE);
		size_t bytes_wrote = write(out_fd, buffer, bytes_read);
		if (bytes_wrote < bytes_read) {
			perror("write");
			exit(1);
		}
		total_bytes_read += bytes_read;
		if (bytes_read < BUFFER_SIZE) {
			printf("Copied 1 partial block\n");
			break;
		} else {
			printf("Copied 1 full block\n");
		}
	}
	printf("Copied %lu bytes in total\n", total_bytes_read);

	pid_t pid = fork();

	if (pid == 0) {
		char* args[] = {".", NULL};
		execvp("/bin/ls", args);
	} else {
		int wstatus;
		wait(&wstatus);
	}

	printf("ls done\n");

	return 0;
}
