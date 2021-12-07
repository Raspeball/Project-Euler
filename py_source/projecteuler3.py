# Import
import math
#
#
# Define functions
#
#
def IsPrime(n):
    # Could write try, except?

    if n <= 1:
        x = float(input("Please enter an integer greater than 2: "))
        i
    if n == 2:
        return True
    else:
        for i in range(2, math.ceil(math.sqrt(n) + 1)):
            if n % i == 0:
                return False

    return True
#
#

def PrimeFactors(n):
    # return the prime factorization of n

    facs = [] # list to hold factors

    f = n

    if IsPrime(f):
        facs.append(f)

    else:
        if f % 2 == 0:
            while f % 2 == 0:
                facs.append(2)
                f = f/2

        i = 3
        while  f > 1 and i <= math.ceil(n/3):
            while f % i == 0:
                facs.append(i)
                f = f/i


            i += 2




    return facs
#
#
#
# Run program
#
#
def main():
    num = 600851475143
    res = PrimeFactors(num)

    print(f"The largest prime facor of {num} is {res[-1]}")

if __name__ == "__main__":
    main()
