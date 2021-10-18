#include <iostream>

int get_fibonacci_last_digit(int n) {
    n = n % 60; // This is because of Pisano Number of 10 is 60
    
    if (n <= 1)
        return n;

    int previous = 0;
    int current  = 1;

    for (int i = 0; i < n - 1; ++i) {
        int tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
    }

    return current % 10;
}

int main() {
    int n;
    std::cin >> n;
    
    int c = get_fibonacci_last_digit(n);
    std::cout << c << '\n';
}
