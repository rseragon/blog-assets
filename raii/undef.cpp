// Common pitfalls

#include <iostream>

class VectorClone  {
public:
  int* _ptr;
  size_t size;

  VectorClone() : _ptr(nullptr), size(0) {}

  void push_back(int i) {
    int* new_ptr = new int[size+1];
    std::copy(_ptr, _ptr + size, new_ptr);
    delete[] _ptr;
    _ptr = new_ptr;
    _ptr[size++] = i;
  }

  int& operator[](size_t index) {
    return _ptr[index];
  }

  ~VectorClone() { delete[] _ptr; }
};

int main() {
  VectorClone v;
  v.push_back(1);

  {
    VectorClone nv = v;
  } // nv destroys v's data here
    // Since nv shallow copies v 
    // This is UB

  std::cout << v[0] << '\n';
}
