#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


int main(int argc, char** argv) {
	
	while(--argc > 1 && !fork());
	sleep(argc = atoi(argv[argc]));
	printf("%d\n", argc);

	return 0;
}
