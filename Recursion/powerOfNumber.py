# 2 ^ 3 = 2 * 2 * 2

def powerOfNumber(n, power):
    if power < 0:
        print("Exponent must be positive")
        return -1
    if power == 0:
        return 1
    else:
        return n * powerOfNumber(n, power-1)


print(powerOfNumber(-2,4))
