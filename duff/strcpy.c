#include <stdio.h>
#include <stdlib.h>

char* strcpy(register char *dst, register const char *src) {
    while ((*dst++ = *src++) != '\0');
    return dst;
}

int main() {
      char* src = "Hello World!";
    char* dst = (char*) malloc(sizeof(char) * (12 + 1));

    strcpy(dst, src);

    printf("%s\n", dst);

    return 0;

}
