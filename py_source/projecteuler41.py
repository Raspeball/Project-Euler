from itertools import permutations
import math

def IsPrime(n):
    if n == 2:
        return True
    else:
        for i in range(2, math.ceil(math.sqrt(n) + 1)):
            if n % i == 0:
                return False

    return True



def InitPerms(pandigstring):
    list_of_pandig = ["".join(i) for i in list(permutations(pandigstring))]

    return list_of_pandig

def DivisibleByThree(list_element):
    digitsum = 0
    for i in list_element:
        digitsum += int(i)
    
    return digitsum % 3 == 0


def ReduceElements(allpermlist):

    temp = []
    for ele in allpermlist:
        if ele[-1] not in ["0","2","4","5","6","8"]:
            temp.append(ele)
    
    # further reduction
    res = [i for i in temp if not DivisibleByThree(i)]

    return res


def TestProblem():
    value = "1234567"
    # value can not be larger
    # since ALL numbers with digits 1-8 and 1-9 are divisible by 3
    # this also applies to 1-5, 1-6, 1-3, and 1-2 (obviously) 
    possible_pandig_primes = ReduceElements(InitPerms(value))


    actual_pandig_primes = []
    for p in possible_pandig_primes:
        if IsPrime(int(p)):
            actual_pandig_primes.append(int(p))
    
    actual_pandig_primes.sort()

    print(actual_pandig_primes)


TestProblem()

