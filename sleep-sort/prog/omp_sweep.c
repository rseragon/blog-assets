#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int c, char **v) {
#pragma omp parallel for num_threads(c)
  for (int i = 1; i < c; ++i) {
    int x = atoi(v[i]);
    sleep(x);
    printf("%d ", x);
  }
}
