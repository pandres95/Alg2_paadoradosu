#include <iostream>

unsigned long long fibonacci_fast(int n) {
    if (n <= 1)
        return n;

    unsigned long long fibonacci_list[n + 1];
    fibonacci_list[0] = 0;
    fibonacci_list[1] = 1;
    
    for (int i = 2; i <= n; i++) {
        fibonacci_list[i] = fibonacci_list[i - 1] + fibonacci_list[i - 2];
    }

    return fibonacci_list[n];
}

int main() {
    int n = 0;
    std::cin >> n;

    std::cout << fibonacci_fast(n) << '\n';
    
    return 0;
}
