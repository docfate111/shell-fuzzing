#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#define LSIZ 15
#define RSIZ 15
#define SIZE 300
int get_installed_shells(char line[15][15]){
    FILE *fptr = NULL; 
    int i = 0;
    fptr = fopen("installed_shells", "r");
    if(fptr==NULL){
        puts("File doesn't exist");
        exit(0);
    }
    while(fgets(line[i], LSIZ, fptr)) {
        line[i][strlen(line[i]) - 1] = '\0';
        i++;
    }
    return i;
}
int run_command(char* cmd, char path[1035]){
    FILE *fp;
    /* Open the command for reading. */
    fp = popen(cmd, "r");
    if (fp == NULL) {
        printf("Failed to run command\n" );
        exit(1);
    }
    /* Get the result and store it in a string */
    int fd = fileno(fp);
    read(fd, path, 1035);
     /* close */
    int exit_code = pclose(fp);
    return exit_code;
}
int main(int argc, char** argv) {
    if(argc != 2){
        printf("Usage [%s] [file to run]", argv[0]);
        return -1;
    }
    char list_of_shells[RSIZ][LSIZ];
    int len = get_installed_shells(list_of_shells);  
    int exit_codes[len];
    char path[1035][len];
    for(int i=0; i<len; i++){
        memset(path[i], 0, 1035);
    }
    for(int i=0; i<len; i++){
        char* cmd = (char*)calloc(15+strlen(argv[1]), sizeof(char));
        strncat(cmd, list_of_shells[i], 15);
        strncat(cmd, " ", 1);
        strncat(cmd, argv[1], 40);
        exit_codes[i] = run_command(cmd, path[i]);
        // exit if exit codes are different
        // is there a more efficient way to do this with less loops?
        for(int a=0; a<=i; a++){
            for(int b=0; b<=i; b++){
               // printf("i=%d, a=%s, b=%s\n", i, path[a], path[b]);
                if(a!=b){
                    if(exit_codes[a]!=exit_codes[b] || strncmp(path[a], path[b], 1035)!=0){
                        puts("Different!");
                        // printf("%s %s\n", path[a], path[b]);
                        // printf("%d %d", exit_codes[a], exit_codes[b]);
                        return -1;
                    }
                }
            }
        }
    }
    return 0;
}
   