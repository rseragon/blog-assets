#include <stdio.h>
#include <stdlib.h>

int* duff(int* dst, const int* src, int len) {
    int n = (len + 3) / 4;

    switch(len % 4) {
        case 0: do { *dst++ = *src++; printf("Case 0\n");
        case 3: *dst++ = *src++; printf("Case 3\n");
        case 2: *dst++ = *src++; printf("Case 2\n");
        case 1: *dst++ = *src++; printf("Case 1\n");
            } while(--n);
    };

    return dst;
}

int main() {
    //int src[] = {1, 2, 8, 4, 5};
    int src[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    int len = sizeof(src)/sizeof(int);
    int dest[len];

    duff(dest, src, len);

    for(int i = 0; i < len; i++)
        printf("%d ", dest[i]);
    printf("\n");
}
