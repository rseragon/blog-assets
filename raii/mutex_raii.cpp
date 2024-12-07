#include <iostream>
#include <mutex>
#include <thread>

static std::mutex mut;

static int glob = 0;

int heavyFunction() { return glob++; }

void bad_foo() {
  mut.lock();

  std::cout << "Incrementing guard(bad_foo) :" << heavyFunction() << std::endl;

  mut.unlock();
}

void good_foo() {

  const std::lock_guard<std::mutex> lg(mut);

  std::cout << "Incrementing guard(good_foo) :" << heavyFunction() << std::endl;

}

int main() {
  
  std::thread t1(good_foo);
  std::thread t2(good_foo);
  std::thread t3(bad_foo);
  std::thread t4(bad_foo);
  
  t1.join();
  t2.join();
  t3.join();
  t4.join();
  
  return 0;
}
