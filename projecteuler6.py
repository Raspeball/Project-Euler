def SumOfSquares(n):
	# n is int
	# range is ok since 0 does not add to res
	# finds the sum of the square of the n first natural numbers
	res = 0
	for i in range(n + 1):
		res += i**2

	return res


# Using the Gauss-formula (triangle numbers) to find the square of the sum #
def SquareOfSum(n):
	# n is int
	# finds the square of the sum of the n first natural numbers
	res = ((n * (n + 1)) / 2)**2
	return res


target = 100 # we want to work with the first 100 natural numbers

diff = SquareOfSum(target) - SumOfSquares(target)

# print result
print(diff)
