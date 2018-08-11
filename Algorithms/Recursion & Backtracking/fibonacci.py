def fibonacci(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1

    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_memoizing(n):

    fib = []
    return cal_fib(n, fib)

def cal_fib(n, fib):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif fib[n]:
        fib[n] = cal_fib(n-1, fib) + cal_fib(n-2, fib)

    return fib[n]


if __name__ == "__main__":
    n = int(input().strip())
    print (fibonacci(n))
    print (fibonacci_memoizing(n))
