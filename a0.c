#include <stdio.h>
#include <string.h>
int main(int argc, char** argv){
    for (int i=1;i<argc;i++){
        int p=0;
        for(int j=0; j<strlen(argv[i]);j++){
            if (argv[i][j] == '-'){
                p++;
            }
        }
    
        for (int k=0;k<=p;k++){
            printf("   ");
        }
        printf("Word: %s \n",argv[i]);
    }
    

    return 0;
}