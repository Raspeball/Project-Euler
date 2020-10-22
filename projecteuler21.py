import numpy as np

def properdivs_sum(x):
	d = 0
	divs = [1]
	for i in range(2,int((np.sqrt(x) + 1))): #start at 2 since 1 is a proper divisor for any number
			if x % i == 0:
				d = d + 1
				divs.append(i)
				if i*i != x:#necessary becayse int(2.99)=2
					divs.append((x / i))
					#
				#
			#
			else:
				continue
				#
			#
	divs.sort()
	sopd = sum(divs)
	return(sopd)
	#
#
#
def amicable_sum(length_num):
	a_sum = 0
	anums = []
	for i in range(length_num):
		if i in anums:
			continue
			#
		else:
			a1 = properdivs_sum(i)
			a2 = properdivs_sum(a1)
			if a2 == a1:
				continue
				#
			elif a2 == i:
				a_sum = a_sum + i + a1#???
				anums.append(i)
				anums.append(a1)
				#
			else:
				continue
				#
			#
		#
	#
	return(a_sum)
	#
#
#
#
pe21_sol = amicable_sum(10000)
print(pe21_sol)
#test = properdivs_sum(284)
#print(test)
