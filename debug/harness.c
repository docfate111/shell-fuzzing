// for asprintf
#define _GNU_SOURCE

#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>

// returns name of file that was output
void run(char *prog, char *file, char **output_file, int *status) {
	asprintf(output_file, "%s_%s.out", prog, file);

	int pid = fork();
	if (pid == 0) {
		// child process
		char *path;
		asprintf(&path, "./%s", prog);

		// set stdout to output file
		int fd = open(*output_file, O_WRONLY | O_CREAT | O_TRUNC, 0644);
		dup2(fd, 1); 

		char **argv = (char **) malloc(sizeof(char *) * 3);
		argv[0] = prog;
		argv[1] = file;
		argv[2] = (char *) 0;

		char **envp = (char **) 0;

		execve(path, argv, envp);
		// NEVER RETURNS
	}

	// parent process
	waitpid(pid, status, 0);
}

int main(int argc, char *argv[]) {
	if (argc != 2) {
		fprintf(stderr, "Usage: %s [filename]\n", argv[0]);
		exit(3);
	}

	char *input_file = argv[1];
	char *prog1_output, *prog2_output;
	int prog1_status, prog2_status;

	run("prog1", input_file, &prog1_output, &prog1_status);
	run("prog2", input_file, &prog2_output, &prog2_status);

	if (prog1_status != prog2_status) {
		printf("statuses differ: prog1 %d prog2 %d\n", prog1_status, prog2_status);
		abort();
	}

	char *diff_cmd;
	asprintf(&diff_cmd, "diff %s %s >/dev/null 2>&1", prog1_output, prog2_output);
	int diff_status = system(diff_cmd);

	if (diff_status != 0) {
		printf("outputs differ\n");
		abort();
	}

	return 0;
}
