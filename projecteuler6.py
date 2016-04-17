hundre = range(1,101)

sqsum = ((101*100)/2)**2
sumsq = 0

for i in range(len(hundre)):
	sumsq += hundre[i]**2

diff = sqsum - sumsq

print diff

		