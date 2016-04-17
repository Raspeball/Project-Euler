# Problem 56
def DigitSum(n):
	dsum = 0
	while n:
		dsum = dsum + n%10
		n = n/10
	return dsum

digitsums = []

for a in range(1,100):
	for b in range(1,100):
		digitsums.append(DigitSum(a**b))

digitsums.sort()

print digitsums[(len(digitsums)-1)]
