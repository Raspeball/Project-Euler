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

OneTwentyEvenlyDivisible()
