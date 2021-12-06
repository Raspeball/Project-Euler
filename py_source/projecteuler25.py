from fibofaster import FiboFaster as ff

n = 1
length = 1

while length < 1000:

    #print(length)
    #print(n)
    n += 1
    length = len(str(ff(n)))

print(f"Fibonacci number {n} is the first with a length of {length} digits")
