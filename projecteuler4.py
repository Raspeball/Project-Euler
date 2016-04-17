num1 = range(100,1000)

num2 = range(100,1000)

prod = [0]

for i in range(len(num1)):
	for j in range(len(num2)):
		prod.append(num1[i]*num2[j])

def palindrome1(x):
	ti5 = x/100000
	ti4 = (x - (ti5*100000))/10000
	ti3 = (x - (ti5*100000) - (ti4*10000))/1000
	ti2 = (x - (ti5*100000) - (ti4*10000) - (ti3*1000))/100
	ti1 = (x - (ti5*100000) - (ti4*10000) - (ti3*1000) -(ti2*100))/10
	ti0 = (x - (ti5*100000) - (ti4*10000) - (ti3*1000) -(ti2*100) - (ti1*10))
	tiere = [ti5,ti4,ti3,ti2,ti1,ti0]
	
	return tiere
	
def palindrome2(y):
	ti5 = y/100000
	ti4 = (y - (ti5*100000))/10000
	ti3 = (y - (ti5*100000) - (ti4*10000))/1000
	ti2 = (y - (ti5*100000) - (ti4*10000) - (ti3*1000))/100
	ti1 = (y - (ti5*100000) - (ti4*10000) - (ti3*1000) -(ti2*100))/10
	ti0 = (y - (ti5*100000) - (ti4*10000) - (ti3*1000) -(ti2*100) - (ti1*10))
	revtiere = [ti0,ti1,ti2,ti3,ti4,ti5]
	
	return revtiere

palindromes = [0]

for z in range(len(prod)):
	if palindrome1(prod[z]) == palindrome2(prod[z]):
		palindromes.append(prod[z])
	else:
		pass

palindromes.sort()

maxpalin = palindromes.pop()

print maxpalin, 'is the largest palindrome product of two three-digit numbers.'


		
			
		
		

