#
# Project Euler #55 #
#
#

def ReverseNum(num):
    rev_num = int(str(num)[::-1])

    return rev_num

def ReverseAdd(num):
    res = num + ReverseNum(num)

    return res


def Lychrel(lim, iterations):

    nLychrel = 0
    isLychrel = None

    for i in range(lim):
        temp_iter = iterations
        x = ReverseAdd(i)

        while temp_iter >= 0:
            if x == ReverseNum(x):
                isLychrel = False
                #print(x)
                break
            else:
                x = ReverseAdd(x)
                #print(x)
                temp_iter = temp_iter - 1
                isLychrel = True

        if isLychrel:
            #print(x)
            nLychrel += 1

    return nLychrel

hailmary = Lychrel(10000, 50)
print(hailmary)
