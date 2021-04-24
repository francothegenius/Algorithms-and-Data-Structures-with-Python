
def sumPreviousNumber(n):
    if n == 1:
        return n
    else:
        return n + sumPreviousNumber(n-1)

print(sumPreviousNumber(5))