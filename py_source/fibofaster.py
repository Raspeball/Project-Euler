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
