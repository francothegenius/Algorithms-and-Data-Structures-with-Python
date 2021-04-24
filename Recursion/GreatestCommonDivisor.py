
def GCD(n1, n2):
    if n1 < 0:
        n1 *= -1
    if n2 < 0:
        n2 *= -1 
    if n2 == 0:
        return n1
    else:
        return GCD(n2 , n1 % n2)

print(GCD(48,18))

