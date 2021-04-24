
def sumOfDigits(n):
    if n < 0:
        print("Number must be positive")
        return -1
    elif n == 0:
        return n
    else:
        return int(n%10) + sumOfDigits(int(n/10))

print(sumOfDigits(99))