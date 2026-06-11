#include <stdio.h>
#include <string.h>
#include <dirent.h>

void ls(char*filepath){
    DIR *dp;
    struct dirent *fp;

    dp=opendir(filepath);

    if(dp == NULL){
        perror("opendir");
    }

    while((fp = readdir(dp))!=NULL){
        printf("%s \n",fp->d_name);

    }
    
    closedir(dp);

}
int main(int argc,char** argv){
    ls(argv[1]);

}

