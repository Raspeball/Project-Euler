#
# Project Euler #52 #
#
# Importing #
import itertools
#
#
def PermutedDigs(num):
    snum = str(num)
    perm_nums = [i for i in itertools.permutations(snum,len(snum))]
    joined_perms = []

    for perms in perm_nums:
        joined_perms.append(int("".join(perms)))
        

    return joined_perms

#test = PermutedDigs(123)
#print(test)

def TimesPermCheck(num):
    timesx = 6
    perms = PermutedDigs(num)

    res = False

    for i in range(timesx):
        num += num
        if num in perms:
            res = True
        else:
            res = False

    return res

for i in range(1, 1000000):
    if TimesPermCheck(i):
        print(i)
    else:
        continue
                
