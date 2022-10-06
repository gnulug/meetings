#define FUSE_USE_VERSION 30
#include <fuse3/fuse.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>


// https://www.cs.hmc.edu/~geoff/classes/hmc.cs135.201109/homework/fuse/fuse_doc.html

#define MESSAGE_LEN 29
char message[MESSAGE_LEN] = "Hello world!\nThis is a test.\n";

int bb_getattr(const char* path, struct stat* stbuf, struct fuse_file_info*) {
	if (strcmp(path, "/") == 0) {
		stbuf->st_mode = S_IFDIR | 0777;
	} else {
		stbuf->st_mode = S_IFREG | 0777;
		stbuf->st_size = MESSAGE_LEN;
	}
	return 0;
}
int bb_open(const char*, struct fuse_file_info*) { return 0; }
int min(int a, int b) { return a < b ? a : b; }
int bb_read(const char*, char* buf, size_t size, off_t offset, struct fuse_file_info* fi) {
	offset = min(MESSAGE_LEN, offset);
	size = min(MESSAGE_LEN - offset, size);
	memcpy(buf, message + offset, size);
	return size;
}
int bb_write(const char*, const char*, size_t size, off_t, struct fuse_file_info*) { return size; }
int bb_readdir(const char*, void* buf, fuse_fill_dir_t filler, off_t, struct fuse_file_info*, enum fuse_readdir_flags) {
	filler(buf, "welcome_to_bbfs", NULL, 0, 0);
	filler(buf, "every_path_resolves_to_a_file", NULL, 0, 0);
	return 0;
}

//////////////////////////////////////////////////////////////////////////////////////////

static const struct fuse_operations bb_oper = {
	.getattr = bb_getattr,
	.open = bb_open,
	.read = bb_read,
	.write = bb_write,
	.readdir = bb_readdir,
};

int main(int argc, char* argv[]) {
	if ((getuid() == 0) || (geteuid() == 0)) {
		fprintf(stderr, "Running this as root opens unnacceptable security holes\n");
		return 1;
	}

	char* prog_name = argv[0];
	if (argc != 2) {
		fprintf(stderr, "Run ./%s <mount point>\n", prog_name);
		return 1;
	}

	char* mount_point = argv[1];
	#define FUSE_ARGC 4
	char* fuse_argv[FUSE_ARGC] = {prog_name, "-d", "-s", mount_point};

	printf("Try running `ls -l %s; ls -l %s/a; cat %s/a; echo a > %s/a`\n", mount_point, mount_point, mount_point, mount_point);
	int fuse_stat = fuse_main(FUSE_ARGC, fuse_argv, &bb_oper, NULL);
	return fuse_stat;
}
