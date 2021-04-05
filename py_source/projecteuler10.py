import primecheck as pc

sum = 0
lim = int(2.0e6)

for i in range(2, lim):
    if pc.IsPrime(i):
        sum += i

    else:
        continue


print(sum)
