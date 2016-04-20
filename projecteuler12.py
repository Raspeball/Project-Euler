def trianglenum(n): #computes the n-th triangle number
	trinum = (n*(n+1))/2
	return trinum

def divnum(x):
	d = 1 # start at 1 since every number has itself as divisor
	if x % 2 == 0:
		for i in range(1,((x/2)+1)):
			if x % i == 0:
				d = d+1
			else:
				continue
	else:
		for i in range(1,((x+1)/2)+1):
			if x % i == 0:
				d = d + 1
			else:
				continue
	return d


def main():
	tnums = 14000 # #-th triangular number
	while tnums >= 1: # >= if you want to start at 1
		triangle = trianglenum(tnums)
		trianglediv = divnum(triangle)
		if trianglediv >= 300:
			break
		else:
			tnums = tnums + 1
		#
	return (triangle, tnums)

print(main())
