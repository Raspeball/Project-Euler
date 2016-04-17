import time
start = time.time()

def main():

	def factorial(number): #only natural numbers
		f = 1
		for i in range(1,(number + 1)):
			f = f*i
		
		return str(f)
	
	num = factorial(100)
	digitsum = 0
	for i in num:
		digitsum = digitsum + float(i)
# -------------- This write-to-file-part is NOT needed, although it works -------------- #	
#	file = open('proj20.txt','w')
#	file.write(num)
#	file.close()
#	
#	file2 = open('proj20.txt','r')
#	for i in range(1,(len(num)+1)):
#		digit = file2.read(1)
#		file2.seek(i,0)
#		digitsum = digitsum + float(digit)
#	file2.close()

	
	print digitsum

main()
end = time.time() - start
print 'Time of execution: ' + str(end) + 's'
	
	