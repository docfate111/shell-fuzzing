#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#define LSIZ 15
#define RSIZ 15
#define SIZE 300
int get_installed_shells(char line[15][15]){
    int i = 0;
    FILE *fptr = fopen("installed_shells", "r");
    if(!fptr){
        puts("File doesn't exist");
        exit(0);
    }
    while(fgets(line[i], LSIZ, fptr)) {
        line[i][strlen(line[i]) - 1] = '\0';
        i++;
    }
    return i;
}
int run_shell(char shellname[], char* filename){
    char* complete_path = (char*)malloc(36);
    strncat(complete_path, "~/smoosh-fuzz/shells/bin/", 25);
    strncat(complete_path, shellname, 11);
    // Fork and fixup STDIN/STDOUT/STDERR.
    int id = fork();
    if(id==0){
        // close stdin/stdout/stderr
        close(stdin);
        close(stderr);
        close(stdout);
        char* complete_path = (char*)malloc(36);
        // open new file for stdin/stdout/stderr
        char* stdinfilename = strdup(shellname);
        strcat(stdinfilename, "stdin");
        char* stdoutfilename = strdup(shellname);
        strcat(stdoutfilename, "stdout");
        char* stderrfilename = strdup(shellname);
        strcat(stderrfilename, "stderr");
        FILE* fstdin = fopen(stdinfilename, "w");
        FILE* fstderr = fopen(stdoutfilename, "w");
        FILE* fstdout = fopen(stderrfilename, "w");
        char* argv[1];
        argv[0] = filename;
        execve(complete_path, argv, NULL);
    }
    // Save STDOUT and STDERR to separate files.
    // Call execve on the given shell with the provided file as an argument.
    // Call wait to get the exit code. Record the exit code in a file.
    // The outer loop that calls fork all of those times should call 
    // wait an equal number of times (or until wait gives up). Then do the comparisons.
}
int main(int argc, char** argv) {
    if(argc != 2){
        printf("Usage [%s] [file to run]", argv[0]);
        return -1;
    } 
    int fd[2];
    if(pipe(fd)==-1){
        perror("Error creating pipe");
        return -1;
    }
    char list_of_shells[RSIZ][LSIZ];
    int num_of_shells = get_installed_shells(list_of_shells);
    for(size_t i=0; i<num_of_shells; i++){
        char* file_to_run = (char*)malloc(12);
        strncpy(file_to_run, argv[1], 11);
        run_shell(list_of_shells[i], file_to_run);
    }
    return 0;
}
