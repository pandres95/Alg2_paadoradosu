import sys

def max_pairwise_product(numbers):
    n = len(numbers)
    
    first = 0
    first_ix = 0
    second = 0

    for i in range(n):
        if numbers[i] > first:
            first = numbers[i]
            first_ix = i
    
    for i in range(n):
        if i != first_ix and numbers[i] > second:
            second = numbers[i]

    return first * second


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = sys.stdin.readline()
    print(max_pairwise_product([int(x) for x in input_numbers.split()]))
