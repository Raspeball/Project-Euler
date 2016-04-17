## --- Projecteuler problem 53 --- ##

import math
import time
start = time.time() 

def main():
	def ncr(n,r):
		res = (math.factorial(n))/((math.factorial(r))*(math.factorial((n-r))))
		
		return res
	
	count = 0
	
	## --- Revised loop (runs just as fast as the old, I think) --- ##
	
	for i in range(100,0,-1): #counting down, let i denote values of n, since n >= r
		for j in range(1,i): #looping values of r, r <= n
			if ncr(i,j) > 1000000:
				count += 1
	
	## --- Old loop --- ##
	
	##for i in range(1,101):
	##	for j in range(100,0,-1): # n goes in the inner loop, since r <= n
	##		if j >= i: #does not need this extra if-statement
	##			if ncr(j,i) > 1000000:
	##				count = count + 1
	##		else:
	##			continue
	
	print count, 'greater than', 1000000

main()

end = time.time() - start
print 'tooktime = ', end, 'seconds'
			