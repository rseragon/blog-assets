#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
  
  char* str = malloc(sizeof(char) * 10);

  strcpy(str, "Some String which will overflow");

  printf("%s\n", str);

  return 0;
}
