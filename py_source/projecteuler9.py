a = range(0,1001)
b = range(1,1001)
c = range(2,1001)

def pyttrip(x,y,z):
	return x**2 + y**2 - z**2

def tripsum(u,v,w):
	return u + v + w


for i in range(len(a)):
	for j in range(len(b)):
		for k in range(len(c)):
			while pyttrip(a[i],b[j],c[k]) == 0 and tripsum(a[i],b[j],c[k]) == 1000:
				while a[i] < b[j] and b[j] < c[k]:
					print a[i], b[j], c[k]
					print a[i]*b[j]*c[k]
					break
				else: pass
				break
			else: pass

			
def SpecialPyt(val):
	
			
