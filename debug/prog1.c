#include <errno.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
	if (argc == 1) {
		 // use STDIN
	} else if (argc == 2) {
		// load argv[1] as STDIN
		int fd = open(argv[1], O_RDONLY);

		if (-1 == fd) {
			fprintf(stderr, "Couldn't open %s: %s\n", argv[1], strerror(errno));
			exit(2);
		}

		dup2(fd, 0);
	} else {
		fprintf(stderr, "Usage: %s [filename] (got %d args)\n", argv[0], argc);
		exit(3);
	}

	char c;
	while (read(0, &c, 1)) {
		write(1, &c, 1);
	}

	return 0;
}
