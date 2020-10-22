import math


def IsPrime(n):
    if n == 2:
        return True
    else:
        for i in range(2, math.ceil(math.sqrt(n) + 1)):
            if n % i == 0:
                return False

    return True

num = 600851475143
facs = []

for i in range(3, math.ceil(math.sqrt(num) + 1)):
    if IsPrime(i):
        if num % i == 0:
            facs.append(i)
        else:
            continue
    else:
        continue

for i in facs:
    print(i)
