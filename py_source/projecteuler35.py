# Project Euler problem 35 #
# https://projecteuler.net/problem=35 #
#
#
#
# Importing #
import math
from itertools import permutations as perm

#

# define function to check if natural number n is prime
def IsPrime(n):
    if n == 2:
        return True
    else:
        for i in range(2, math.ceil(math.sqrt(n) + 1)):
            if n % i == 0:
                return False

    return True
    #
#

# define a simple function to check if a number n
# in fact _can_ have a full rotation where all rotations are prime
# any number containing the digits 0, 2, 4, 6 or 8 can not
def FullRotationPrimeCheck(n):

    if n == 2:
        return True
    
    else:
        for i in range(0, 9, 2):
            if str(i) in str(n):
                return False
    
        return True
        

# define function that finds all full rotations of a number
def FullRotation(n):
    #
    poss = FullRotationPrimeCheck(n)
    if poss:
        # SHIFT ALL ONE TO THE LEFT UNTIL WE REACH SAME NUMBER AS WE STARTED WITH
        temp = list(str(n))
        list_perm = []
        shift = 1
        for i in range(1, (len(str(n)) + 1)):
            x = [None]*len(temp)
            x[shift - i] = temp[i]
            list_perm += temp





    # OLD VERSION #
    #     list_perm = ["".join(p) for p in perm(str(n), len(str(n)))]

    #     # removing doubles
    #     #list_perm[:] = [p for p in set(list_perm)]

    #     diff = len(str(n)) - len(set(str(n))) # diff always >= 0

    #     if diff == 0:
    #         for i, j in enumerate(str(n)):
    #             list_perm[:] = [p for p in list_perm if p[i] != j]
        
    #     else:
    #         list_perm[:] = [p for p in set(list_perm)]
    
    # else:
    #     list_perm = []

    
    # list_perm[:] = [p for p in set(list_perm)] # removing doubles
    
    # list_perm[:] = [eval(ele) for ele in list_perm] # integers
    # END OLD VERSION #


    return poss, list_perm
    #
#

# define function to check if all full rotations of a number are primes
def IsCircularPrime(n):
    circ_poss, rot_list = FullRotation(n)

    if circ_poss:
        for ele in rot_list:
            if not IsPrime(ele):
                return False
        
        return True

    else:
        return False
        #
    #
#
#

# main
## FIX: Program returns 25 for all values > 1000
## Answer should be 55
def main():
    # goal = 10000
    # count = 0
    # primes = [p for p in range(2, goal + 1) if IsPrime(p)]
    # #print(primes)

    # for n in primes:
    #     if IsCircularPrime(n):
    #         #print(n) # for testing
    #         count += 1
    
    # print(count)

    # TESTING #
    # test = FullRotationPrimeCheck(1171)
    # print(test)
    x, y = FullRotation(197) # 13337
    print(y)
    # END TESTING #
#
#
# run program #
if __name__ == '__main__':
    main()



