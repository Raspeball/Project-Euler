#
# Importing #
import math


# Simple shift-function
RotNum = lambda numstr, shift : [numstr[i - shift] for i in range(len(numstr))]

# Check if num is prime

def IsPrime(num):


n_circ_primes = 0

for i in range(2, 1000000):
    num = str(i)
    for j in range(len(num)):
        if IsPrime(num):
            while IsPrime(num):
                num = RotNum(
