# import #
from tqdm import tqdm
#
#
#
def Collatz(n):
	num = 1
	while n != 1:
		if n % 2 == 0:
			n = n/2
		else:
			n = 3*n + 1
		num = num + 1

	return num


def CollatzSequence(number_lim):
	topnum = 0
	topseq = 0
	for i in tqdm(range(2, number_lim + 1)):
	#for i in range(2,number_lim + 1):
		if Collatz(i) > topseq:
			topseq = Collatz(i)
			topnum = i
		else:
			continue
	return topnum

def main():
	lim = 1000000

	res = CollatzSequence(lim)
	print(res)

if __name__ == '__main__':
	main()
