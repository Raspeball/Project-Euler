# Problem 29
#We want a,b >= 2 and a,b <= 100
powerlist = []

for x in range(2,101):
	for y in range (2,101):
		powerlist.append(x**y)

powerlist = set(powerlist)

powercount = len(powerlist)

print powercount
