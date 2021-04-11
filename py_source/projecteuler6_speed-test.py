import numpy as np
import timeit


def SumOfSquares(n=1000000):
	# n is int
	# range is ok since 0 does not add to res
	# finds the sum of the square of the n first natural numbers
	res = 0
	for i in range(n + 1):
		res += i**2

	return res


def SumOfSquaresList(n=1000000):

	return sum([i**2 for i in range(n+1)])


def SumOfSquaresNP(n=1000000):
	x = np.arange(n+1)
	return np.sum(x**2)


# Using the Gauss-formula (triangle numbers) to find the square of the sum #
def SquareOfSum(n):
	# n is int
	# finds the square of the sum of the n first natural numbers
	res = ((n * (n + 1)) / 2)**2
	return res


#target = 100 # we want to work with the first 100 natural numbers

#diff = SquareOfSum(target) - SumOfSquares(target)

# print result
#print(diff)


def speedtest():
	print("original: {}".format(timeit.timeit(SumOfSquares, number=1)))
	print("list: {}".format(timeit.timeit(SumOfSquaresList, number=1)))
	print("np: {}".format(timeit.timeit(SumOfSquaresNP, number=1)))

speedtest()
