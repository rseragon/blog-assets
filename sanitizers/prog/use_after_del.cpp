#include <iostream>

int main() {

	int *a = new int[3];

	delete [] a;

	a[1] = 100;

	std::cout << a [1] << '\n';

	return 0;
}
