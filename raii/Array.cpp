#include <cstddef>   // size_t
#include <stdexcept> // std::out_of_range

#include <iostream>

class Array {
public:
  int*   arr  = nullptr;
  size_t size = 0; // Capacity
  size_t len  = 0; // Current length

  Array(size_t s = 0) 
    : arr(new int[s]), size(s) {}

  void push_back(int val) {
    if(len+1 >= size)
      throw std::out_of_range("Size exceeded");
    arr[len++] = val;
  }

  ~Array() { delete[] arr; }
};

int main() {
  Array arr = Array();

  try {
    arr.push_back(1);
  }
  catch(...) {
    std::cout << "size exceed\n";
  }
}
