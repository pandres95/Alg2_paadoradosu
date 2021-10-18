# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    n = n % 60 # This is because of Pisano Number of 10 is 60
    
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
