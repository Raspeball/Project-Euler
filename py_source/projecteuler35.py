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

# define function that finds all full rotations of a number
def Rotation(n):
    #
    list_perm = ["".join(p) for p in perm(str(n), len(str(n)))]
    #
    #
    if len(set(str(n))) > len(str(n)) - 1:
        
        # removing
        for i, j in enumerate(str(n)):
            list_perm[:] = [p for p in list_perm if p[i] != j]
    
        # cast out leading 0
        #list_perm[:] = [ele for ele in list_perm if ele[0] != "0"]
        # 
        list_perm.append(str(n))
    
    else:
        list_perm[:] = [p for p in set(list_perm)]
        
    # integers
    list_perm[:] = [eval(ele) for ele in list_perm]


    return list_perm
    #
#

# define function to check if all full rotations of a number are primes
def IsCircularPrime(n):
    rot_list = Rotation(n)

    for ele in rot_list:
        if not IsPrime(ele):
            return False
    
    return True
    #
#

# main
## FIX: Program returns 25 for all values > 1000
## Answer should be 55
def main():
    goal = 1500
    count = 0
    primes = [p for p in range(2, goal + 1) if "0" not in str(p) and IsPrime(p)]
    #print(primes)

    for n in primes:
        if IsCircularPrime(n):
            #print(n) # for testing
            count += 1
    
    print(count)
    #
    # test = Rotation(887)
    # print(test)
    # test2 = IsCircularPrime(887)
    # print(test2)
#
#
# run program #
if __name__ == '__main__':
    main()



