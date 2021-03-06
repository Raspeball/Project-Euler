import math
import collections


def PropDiv(num):
    propdivs = [1]
    r = num

    for i in range(2, int(math.ceil(num/2.0))):
        if r % i == 0:
            propdivs.append(int(r/i))
            propdivs.append(int(i))
            r = r/i

    #  print(propdivs)

    multiples = collections.Counter(propdivs)

    for m in multiples.keys():
        if multiples[m] > 1:
            for n in range(2, multiples[m] + 1):
                if m**n != num and m**n < num:
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

limit = 28123
#  Testing yield 1047 abundant numbers under this limit
