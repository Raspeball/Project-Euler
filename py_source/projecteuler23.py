import math
import collections
from itertools import combinations


def PropDiv(num):
    propdivs = [1]
    r = num

    for i in range(2, int(math.ceil(num/2.0))):
        if r % i == 0:
            propdivs.append(int(r/i))
            propdivs.append(int(i))
            #r = r/i

    #  print(propdivs)

    multiples = collections.Counter(propdivs)

    for m in multiples.keys():
        if multiples[m] > 1:
            for n in range(2, multiples[m] + 1):
                if m**n != num and m**n < num:
                    if m**n % num == 0:
                        propdivs.append(m**n)


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

    for num in range(13, upper_lim - 11):
        if IsAbundant(num):
            abundant_nums.append(num)
        else:
            continue

    return abundant_nums

def NotSumOfTwoAbundant(limit):
    abundant = AbundantNumbers(limit)
    sum_two_ab = []

    for ab_pair in combinations(abundant, 2):
        sum_two_ab.append(sum(ab_pair))
    
    excl = [i for i in range(1, limit) if i not in sum_two_ab]

    return excl

limit = 28123
res = sum(NotSumOfTwoAbundant(limit))
print(res)
