#include <iostream>

long long gcd(long long a, long long b) {
  if (b == 0) {
    return a;
  }

  return gcd(b, a % b);
}

long long lcm(long long a, long long b) {
  return (long long) a * b / gcd(a, b);
}

int main() {
  long long a, b;
  
  std::cin >> a >> b;
  std::cout << lcm(a, b) << std::endl;
  
  return 0;
}
