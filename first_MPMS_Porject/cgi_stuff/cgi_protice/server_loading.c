#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/* 取得 server 的 loading
 */
int get_server_loading()
{
        int loading = 0;
        srand (time(NULL));
        loading = rand() % 100;
}

int main()
{
        printf ("Content-type: text/xml\n\n");
        printf ("<ajax-response>\n");
        printf ("<response type=\"object\" id=\"loadUpdater\">\n");
        printf ("<cpu load=%d/>\n", get_server_loading());
        printf ("</response>\n");
        printf ("</ajax-response>\n");
}
