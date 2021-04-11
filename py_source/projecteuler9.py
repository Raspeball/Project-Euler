import numpy as np
import itertools
import timeit


def IsPytTriple(a, b, c):

	l = [a**2, b**2, c**2]
	perm = itertools.permutations(l)
	res = False

	for i in list(perm):
		if i[0] + i[1] == i[2]:
			res = True
		else:
			continue

	return res

def SpecialPyt(val):

	x = np.arange(1, val+1)



	for i in x:
		for j in x:
			k = val - (i + j)
			if IsPytTriple(i,j,k):
				return i*j*k
			else:
				continue

print(SpecialPyt(1000))
