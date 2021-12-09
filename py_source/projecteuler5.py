# import
import numpy as np
#
#
# Define functions
def EvenlyDivisibleManual(n):
	# funnction using a for loop

	d = 1
	for i in range(1, n+1):
		d = np.lcm(d, i)

	return d

# Function using numpy built in
def EvenlyDivisible(n):

	res = np.lcm.reduce(range(1, n+1))

	return res

print(EvenlyDivisibleManual(20))
print(EvenlyDivisible(20))

#
# Alternative specific to this problem
#
#
#Does not need any code to do this, really.
# 2520 is divisible with numbers 1-10
# Then, you need a factor 2 for 20 and 16 (2*8), and then the primes 11,13,17,19
# Done!

#ans = 2520*2*11*13*17*19
#print(ans)
