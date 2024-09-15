import math

def IncreasingNum(n):

    x = str(n)

    for i in range(1, len(x)):
        if x[i] >= x[i-1]:
            return True
        else:
            return False
            break

def DecreasingNum(n):

    x = str(n)

    for i in range(1, len(x)):
        if x[i] <= x[i-1]:
            return True
        else:
            return False
            break

test = 66420

def PropBouncy():

    nTot = 21781
    nBouncy = 19602 # (nTot-1)*0.9
    
    threshold = 0.99

    while nTot > 21780:
        if IncreasingNum(nTot) == False and DecreasingNum(nTot) == False:
            nBouncy += 1

        if (nBouncy/nTot) == threshold:
            print(nTot)
        else:
            continue


PropBouncy()


        
        
        
