def main():
	value = 4000000
	sum = 2
	fibo = [0]*value
	fibo[0] = 1
	fibo[1] = 2
	f = 0
	for i in range(2,value):
		f = fibo[i-2] + fibo[i-1]
		if f > value:
			break
		if f % 2 == 0:
			sum = sum + f

		fibo[i] = f

	print sum	
	
main()
		