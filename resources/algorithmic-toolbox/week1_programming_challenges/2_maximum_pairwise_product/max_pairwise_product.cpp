#include <iostream>
#include <vector>
#include <algorithm>

int MaxPairwiseProduct(const std::vector<int>& numbers) {
    int max_product = 0;
    int n = numbers.size();

    int first = 0, first_ix = 0, second = 0;

    for (int i = 0; i < n; i++) {
        if (numbers[i] > first) {
            first = numbers[i];
            first_ix = i;
        }
    }
    
    for (int i = 0; i < n; i++) {
        if (i != first_ix && numbers[i] > second) {
            second = numbers[i];
        }
    }

    return first * second;
}

int main() {
    int n;
    std::cin >> n;
    std::vector<int> numbers(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> numbers[i];
    }

    std::cout << MaxPairwiseProduct(numbers); << "\n";
    return 0;
}
