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


def Lychrel(num, iterations):

    nLychrel = 0
    temp_iter = iterations
    x = num
    #for i in range(lim):
    while temp_iter >= 0:
        if x == ReverseNum(x):
            break
        else:
            x = ReverseAdd(x)
            print(x)
            temp_iter = temp_iter - 1

    if temp_iter == 0:
        nLychrel += 1
        temp_iter = iterations

    return nLychrel

Lychrel(349, 50)

    

        
                
            
            
    
