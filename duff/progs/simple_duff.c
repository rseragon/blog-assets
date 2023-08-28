#include <stdio.h>
#include <stdlib.h>

int* duff(int* dst, const int* src, int len) {
    int n = (len + 7) / 8;

    switch(len % 8) {
        case 0: do {
        case 7: *dst++ = *src++;
        case 6: *dst++ = *src++;
        case 5: *dst++ = *src++;
        case 4: *dst++ = *src++;
        case 3: *dst++ = *src++;
        case 2: *dst++ = *src++;
        case 1: *dst++ = *src++;
            } while(--n);
    };

    return dst;
}

int main() {
    int src[] = {1, 2, 8, 4, 5};
    int len = sizeof(src)/sizeof(int);
    int dest[len];

    duff(dest, src, len);

    for(int i = 0; i < len; i++)
        printf("%d ", dest[i]);
    printf("\n");
}
