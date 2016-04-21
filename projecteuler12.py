import numpy as np

def trianglenum(n): #computes the n-th triangle number
	trinum = (n*(n+1))/2
	return trinum

def divnum(x):
	d = 0
	largeds = []
	for i in xrange(1,int((np.sqrt(x) + 1))):
			if x % i == 0:
				d = d + 1
				if i*i != x:
					largeds.append((x / i))
			else: continue
	totd = d + len(largeds)
	return totd


def main():
	tnums = 1 # #-th triangular number
	while tnums >= 1:
		triangle = trianglenum(tnums)
		trianglediv = divnum(triangle)
		if trianglediv >= 500:
			break
		else:
			tnums = tnums + 1
		#
	return (triangle, tnums)

print(main())
