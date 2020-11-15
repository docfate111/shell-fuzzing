#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#define LSIZ 15
#define RSIZ 15
#define SIZE 300
int get_installed_shells(char line[15][15]){
    int i = 0;
    FILE *fptr = fopen("installed_shells", "r");
    if(!fptr){
        perror("Please include a file named \"installed_shells\"");
        exit(0);
    }
    while(fgets(line[i], LSIZ, fptr)) {
        line[i][strlen(line[i]) - 1] = '\0';
        i++;
    }
    return i;
}
int run_shell(char* shellname, char* filename){
    char* complete_path = (char*)malloc(52);
    strncat(complete_path, "/Users/thwilliams/smoosh-fuzz/shells/bin/", 41);
    strncat(complete_path, shellname, 11);
    char* args[3] = {complete_path, filename, NULL};
    int status;
    //, exitcode;
    // Fork and fixup STDIN/STDOUT/STDERR.
    if(fork()==0){
        // close stdin/stdout/stderr
        // open new file for stdin/stdout/stderr
        char* stdinfilename = strdup(shellname);
        strcat(stdinfilename, "stdin");
        char* stdoutfilename = strdup(shellname);
        strcat(stdoutfilename, "stdout");
        char* stderrfilename = strdup(shellname);
        strcat(stderrfilename, "stderr");
        // renumber file descriptors
        int fstdin = open(stdinfilename, O_WRONLY | O_CREAT | O_TRUNC, 0644);
        int fstderr = open(stderrfilename, O_WRONLY  | O_CREAT | O_TRUNC, 0644);
        int fstdout = open(stdoutfilename, O_WRONLY  | O_CREAT | O_TRUNC, 0644);
        if(dup2(fstdin, 0)==-1){
            perror("Error duplicating stdin");
        }
        if(dup2(fstdout, 1)==-1){
             perror("Error duplicating stdout");
        }
        if(dup2(fstderr, 2)==-1){
            perror("Error duplicating stderr");
        }
        wait(&status);
        if(!WIFEXITED(status)){
            perror("Error getting the exit code");
        }
        if(execve(args[0], args, NULL)==-1){
            perror("Error running execve");
        }
        return WEXITSTATUS(status);
    }
    // Call wait to get the exit code. Record the exit code in a file.
    // The outer loop that calls fork all of those times should call 
    // wait an equal number of times (or until wait gives up). Then do the comparisons.
    return 0;
}
int main(int argc, char** argv) {
    if(argc != 2){
        printf("Usage [%s] [file to run]", argv[0]);
        return -1;
    }
    char list_of_shells[RSIZ][LSIZ];
    int num_of_shells = get_installed_shells(list_of_shells);
    int exitcodes[LSIZ];
    for(int i=0; i<num_of_shells; i++){
        char* file_to_run = (char*)malloc(12);
        strncpy(file_to_run, argv[1], 11);
        exitcodes[i] = run_shell(list_of_shells[i], file_to_run);
    }
    return 0;
}
