import math
from primecheck import IsPrime

def QuadPrimeFormula(n, a, b):

    res = n**2 + a*n + b

    return res


def QuadPrimeSeqLenght(n, a, b):

    seq_len = 0
    try:
        while IsPrime(QuadPrimeFormula(n, a, b)):
            seq_len += 1
            n += 1

    except ValueError:
        seq_len = 0

    return seq_len


## Test ##
max_len = 0
max_a = 0
max_b = 0
for b in range(-1000, 1001, 1):
    for a in range(-999, 1000, 1):
        temp_len = QuadPrimeSeqLenght(0, a, b)
        if temp_len > max_len:
            max_len = temp_len
            max_a, max_b = a, b

        else:
            continue

print(f"{max_a*max_b}")
