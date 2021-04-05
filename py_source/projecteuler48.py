## --- Projecteuler problem 48 --- ##

import time
start = time.time() 	

def main():
	def selfpower(power):
		selfpownum = 0
		for i in range(1,(power + 1)):
			selfpownum = selfpownum + (i**i)
		
		return selfpownum
	
	proj48 = selfpower(1000)
	lasttentxt = str(proj48)[-10:]
	
	print lasttentxt

main()

end = time.time() - start
print 'tooktime = ', end, 'seconds'