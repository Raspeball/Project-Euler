def Collatz(n):
	num = 1
	while n != 1:
		if n % 2 == 0:
			n = n/2
		else:
			n = 3*n + 1
		num = num + 1
	
	return num
	

def CollatzNum():
	topnum = 0
	topseq = 0
	for i in range(2,1000001):
		if Collatz(i) > topseq:
			topseq = Collatz(i)
			topnum = i
		else:
			continue
	return topnum

print(CollatzNum())

	
	
	
		
		