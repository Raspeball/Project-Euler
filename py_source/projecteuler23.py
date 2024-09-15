import math
import collections
from itertools import combinations_with_replacement as iter_cwr


def PropDiv(num):
    propdivs = [1]
    #r = num

    n = int(math.ceil(math.sqrt(num)))

    for i in range(2, n):
        if num % i == 0:
            propdivs.append(int(num/i))
            propdivs.append(int(i))

    if n**2 == num:
        propdivs.append(n)


    propdivs = list(set(propdivs))


    return propdivs


def IsPerfect(num):
    divisor_sum = sum(PropDiv(num))

    if divisor_sum == num:
        return True
    else:
        return False


def IsAbundant(num):
    divisor_sum = sum(PropDiv(num))

    if divisor_sum > num:
        return True
    else:
        return False

def AbundantNumbers(upper_lim):
    abundant_nums = [12] # 12 is the lowest abundant number

    for num in range(13, upper_lim):
        if IsAbundant(num):
            abundant_nums.append(num)
        else:
            continue

    return abundant_nums

def NotSumOfTwoAbundant(limit):
    abundant = AbundantNumbers(limit)
    sum_two_ab = []

    for ab_pair in iter_cwr(abundant, 2):
        sum_two_ab.append(sum(ab_pair))
    
    excl = [i for i in range(1, limit) if i not in sum_two_ab]

    return excl

limit = 28123
res = sum(NotSumOfTwoAbundant(limit))
print(res)