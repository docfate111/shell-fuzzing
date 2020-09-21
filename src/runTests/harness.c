#include <stdio.h>
#include <stdlib.h>
#include <string.h>
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
void run_command(char* cmd){
    FILE *fp;
    char path[1035];
        /* Open the command for reading. */
    fp = popen(cmd, "r");
    if (fp == NULL) {
        printf("Failed to run command\n" );
        exit(1);
    }
    /* Read the output a line at a time - output it. */
    while (fgets(path, sizeof(path), fp) != NULL) {
        printf("%s\n", path);
    }
     /* close */
    printf("%d exit status\n", pclose(fp));
    // TODO: get stderr and compare structs of exit code, STDOUT, and STDERR
}
int main(int argc, char** argv) {
    if(argc != 2){
        printf("Usage [%s] [file to run]", argv[0]);
        return -1;
    }
    char list_of_shells[RSIZ][LSIZ];
    int len = get_installed_shells(list_of_shells);  
    for(int i=0; i<len; i++){
        char* cmd = (char*)malloc(15+strlen(argv[1]));
        strncat(cmd, list_of_shells[i], 15);
        strcat(cmd, " ");
        strncat(cmd, argv[1], 40);
        run_command(cmd);
    }
    return 0;
}
   