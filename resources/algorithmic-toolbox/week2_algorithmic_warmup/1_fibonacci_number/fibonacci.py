# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    f_list = [0, 1]
    
    for i in range(2, n + 1):
        f_list.append(f_list[i - 1] + f_list[i - 2])

    return f_list[n]

n = int(input())
print(calc_fib(n))
