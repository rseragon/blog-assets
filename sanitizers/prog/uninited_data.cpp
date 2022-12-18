#include <vector>
#include <iostream>
int main(int argc, char** argv) {
	std::vector<int> vec{10};
	std::cout << vec[argc] << '\n';
	// ...
}
