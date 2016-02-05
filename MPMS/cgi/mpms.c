#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
    time_t current;
    struct tm *timeinfo;
    time(&current);
    int people_num = 18;

    FILE *pFile;
    char buffer[1024];

    timeinfo = localtime(&current);

    //access
    printf("Content type: text/html\n\n");

    //printf("%s\n", asctime(timeinfo));

    //printf("People num: %d\n", people_num);

    pFile = fopen("/home/pi/MPMS/node_record_sum.txt", "r");

    if( NULL == pFile){
        printf("open file fail...\n");
        return 1;
    }else{
        fread(buffer, 1024, 1, pFile);
        printf("%s\n", buffer );
    }

    fclose(pFile);

    return 0;
}