import math

def IsPrime(n):
    if n == 2:
        return True
    else:
        for i in range(2, math.ceil(math.sqrt(n) + 1)):
            if n % i == 0:
                return False

    return True

count = 0
n = 1
while count <= 10001:

    if IsPrime(n):
        count += 1

    n += 1

print(n-1)
