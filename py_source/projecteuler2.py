
# Function that returns the n-th fibonacci-number
# recursive function
def Fibo(n):

	if n == 0:
		return 0

	elif n == 1:
		return 1

	else:
		return Fibo(n-1) + Fibo(n-2)

# Non-recursive function
# returns the n-th fibonacci-number
def FiboFaster(n):
	a = 0
	b = 1

	if n == 0:
		return 0

	elif n == 1:
		return 1

	else:
		for i in range(1, n):
			f = a + b
			a = b
			b = f

		return b

lim = 4000000
sum_even_fibo = 0

for i in range(lim):
	fib = FiboFaster(i)

	if fib > lim:
		break
	else:
		if fib % 2 == 0:
			sum_even_fibo += fib
#while curr_fibo < lim:
#	if curr_fibo % 2 == 0:
#		sum_even_fibo = sum_even_fibo + curr_fibo
#
#	ledd += 1

print(sum_even_fibo)
