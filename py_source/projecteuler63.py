#
# Project Euler #63 #
#
# Importing #
import math
#
#

def PowerfulDigit(power):

    res = 20

    digpowers = [i**power for i in range(2, 9)]
    
    start = int(math.pow(10, (power - 1)))
    stop = int(math.pow(10, power) - 1)

    for i in range(start, stop):
        if i in digpowers:
            res += 1

        else:
            continue

    return res
#
#

n_digit_also_pow = 0

for i in range(2, 11):
    n = PowerfulDigit(i)
    n_digit_also_pow += n

print(n_digit_also_pow)

    
