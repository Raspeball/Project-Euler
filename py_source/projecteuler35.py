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
        # shift one to the left until we return to n
        list_full_rot = [str(n)] # add n to the list of full rotations

        for i in range(1, len(str(n))):
            full_rot = str(n)[i:] + str(n)[:i]
            list_full_rot.append(full_rot)
        
        list_full_rot[:] = [p for p in set(list_full_rot)] # removing doubles
        
        list_full_rot[:] = [eval(ele) for ele in list_full_rot] # integers
    
    else:
        list_full_rot = []    
    

    return poss, list_full_rot
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
def main():
    goal = 1000000
    count = 0
    primes = [p for p in range(2, goal + 1) if IsPrime(p)]
    #print(primes)

    for n in primes:
        if IsCircularPrime(n):
            #print(n) # for testing
            count += 1
    
    print(count)

    # TESTING #
    # x, y = FullRotation(197)
    # print(y)
    # END TESTING #
#
#
# run program #
if __name__ == '__main__':
    main()



