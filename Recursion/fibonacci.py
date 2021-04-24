
def fibonacci(n):
    if n < 0:
        print("Fibonacci not defined for negative numbers")
        return -1
    elif n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))
