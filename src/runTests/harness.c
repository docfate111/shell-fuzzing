#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define SIZE 1000
/* following the docs: 
 https://github.com/mykter/afl-training/tree/master/harness
*/
void compare(char* s1, char* s2){
    puts(s1);
    puts(s2);
    // char input[SIZE] = {0};
    // read(0, input, SIZE);
}
int main(int argc, char* argv[]){
    if(argc<3){
        printf("Usage %s [first shell] [other shell]", argv[0]);
        return 1;
    }
    char* shell1 = (char*)malloc(10);
    char* shell2 = (char*)malloc(10);
    strncpy(shell1, argv[1], 10);
    strncpy(shell2, argv[2], 10);
    compare(shell1, shell2);
    return 0;
}