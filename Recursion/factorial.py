
def factorial(n):
    if n < 0:
        print("Number for factorial must be positive")
        return -1
    elif n < 1:
        return 1
    else:
        ans = n * factorial(n-1)
        return ans


print(factorial(-1))
print(factorial(1))
print(factorial(10))
print(factorial(5))