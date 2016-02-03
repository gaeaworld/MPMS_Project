#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[], char *envp[])
{
   printf("Content-type: text/html\n\n");
   int length=atoi(getenv("CONTENT_LENGTH"));
   printf("length=%d\n", length);
   char format[20], post[10000];
   sprintf(format, "%%%dc", length); 
   scanf(format, post);
   printf("post=%s", post);
}
