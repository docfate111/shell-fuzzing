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
int diff(char* shell1, char* shell2){
    // exit code of 1 if different
    char* complete_path = "/usr/bin/diff";
    // set up files to check
    char* stdinfilename = strdup(shell1);
    strcat(stdinfilename, "stdin");
    char* stdoutfilename = strdup(shell1);
    strcat(stdoutfilename, "stdout");
    char* stderrfilename = strdup(shell1);
    strcat(stderrfilename, "stderr");
    char* shell1files[] = {stdinfilename, stdoutfilename, stderrfilename};
    char* stdinfilename2 = strdup(shell2);
    strcat(stdinfilename2, "stdin");
    char* stdoutfilename2 = strdup(shell2);
    strcat(stdoutfilename2, "stdout");
    char* stderrfilename2 = strdup(shell2);
    strcat(stderrfilename2, "stderr");
    char* shell2files[] = {stdinfilename2, stdoutfilename2, stderrfilename2};
    int exitcode = 0;
    int status;
    for(size_t i=0; i<3; i++){
        char* args[] = {complete_path, shell1files[i], shell2files[i], NULL};
        if(fork()==0){
            wait(&status);
            if(!WIFEXITED(status)){
                perror("Error getting the exit code");
            }
            if(execve(args[0], args, NULL)==-1){
                perror("Error running execve");
            }
            exitcode |= WEXITSTATUS(status);
        }
    }
    return exitcode;
}
int run_shell(char* shellname, char* filename){
    char* complete_path = (char*)malloc(52);
    strncat(complete_path, "/Users/thwilliams/smoosh-fuzz/shells/bin/", 41);
    strncat(complete_path, shellname, 11);
    char* args[3] = {complete_path, filename, NULL};
    int status;
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
        // Call wait to get the exit code. Record the exit code in a file.
        wait(&status);
        if(!WIFEXITED(status)){
            perror("Error getting the exit code");
        }
        if(execve(args[0], args, NULL)==-1){
            perror("Error running execve");
        }
        return WEXITSTATUS(status);
    }
    return 0;
}
int main(int argc, char** argv) {
    if(argc != 2){
        printf("Usage [%s] [file to run]", argv[0]);
        return -1;
    }
    char list_of_shells[RSIZ][LSIZ];
    int num_of_shells = get_installed_shells(list_of_shells);
    int exitcodes[num_of_shells];
    for(int i=0; i<num_of_shells; i++){
        char* file_to_run = (char*)malloc(12);
        strncpy(file_to_run, argv[1], 11);
        exitcodes[i] = run_shell(list_of_shells[i], file_to_run);
    }
    // compare exit codes
    for(int i=0; i<num_of_shells; i++){
        for(int j=0; j<num_of_shells; j++){
            if(exitcodes[i]!=exitcodes[j]){
                printf("Different exit codes: %d!=%d", exitcodes[i], exitcodes[j]);
                return 1;
            }
        }
    }
    // compare files
    for(int i=0; i<num_of_shells; i++){
        for(int j=0; j<num_of_shells; j++){
            if(i!=j){
                if(diff(list_of_shells[i], list_of_shells[j])){
                    printf("Different stdout, stderr, or stdin!");
                }
            }
        }
    }
    return 0;
}
