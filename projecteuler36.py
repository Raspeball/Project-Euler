#
# Project Euler 36 #
# Double-base palindromes #

#
# Importing #
#


def IsPalin(num):
    x = str(num)

    if x[0] == "0":
        if x[1] == "b":
            x = x[2:len(x)]
        else:
            return False

    if x == x[::-1]:
        return True
    else:
        return False

db_palin_sum = 0 # sum of all double-base palindromes

for i in range(1, 1000000):
    b = bin(i)
    if IsPalin(i) and IsPalin(b):
        db_palin_sum += i
    else:
        continue

print(db_palin_sum)
