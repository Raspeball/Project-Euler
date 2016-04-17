def trianglenum(n): #computes the n-th triangle number
	trinum = n*(n+1)
	return trinum

def divnum(x):
	d = 0
	for i in range(1,(x+1)):
		if x % i == 0:
			d = d +1
		else:
			continue
	return d


def main():
	tnums = 8
	while tnums > 1:
		triangle = trianglenum(tnums)
		trianglediv = divnum(tnums)
		if trianglediv >= 500:
			return triangle
			break
		else:
			tnums = tnums +1
	
	print triangle

main()
		