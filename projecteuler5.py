def OneTwentyEvenlyDivisible():
	divs = range(1,21)
	startnum = 2520
	minnum = 0
	while startnum >= 1:
		for i in divs:
			if startnum % i == 0:
				minnum = startnum
				break
			else:
				startnum = startnum + 1
	return startnum

#OneTwentyEvenlyDivisible()

#Does not need any code to do this, really.
# 2520 is divisible with numbers 1-10
# Then, you need a factor 2 for 20 and 16 (2*8), and then the primes 11,13,17,19
# Done!

ans = 2520*2*11*13*17*19

print(ans)
