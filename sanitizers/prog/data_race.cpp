// -fsanitizer=thread -g
#include <iostream>
#include <thread>

int GLOBAL = 0;

void update_global() {
	GLOBAL++;	
	std::cout << "From thread: " << GLOBAL << '\n';
}

int main() {
	std::thread t{update_global};
	GLOBAL++;

	std::cout << "From main: " << GLOBAL << '\n';
	t.join();


	std::cout << "Final: " << GLOBAL << '\n';
	return 0;
}
