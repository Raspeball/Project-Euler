import math
#
#

def ErPrimtall(tall):
    prime = 1
    grense = int(math.sqrt(tall)) + 1
    
    if tall < 2:
        prime = 0
    else:
        for i in range(2, grense):
            if tall % i != 0:
                prime = prime*True
            else:
                prime = prime*False
    return bool(prime)



def OddeSammensatt(tall):
    if tall % 2 == 1:
        if not ErPrimtall(tall):
            return True
        else:
            return False
    else:
        return False
    
def GoldbachAndre(tall):
    
    res = False
    
    if OddeSammensatt(tall):
        upper = tall - 2
        for i in range(2, upper + 1, 1):
            if ErPrimtall(i):
                rest = math.sqrt((tall - i)/2)
                if rest**2 == (int(rest))**2:
                    res = True
                else:
                    continue
            else:
                continue
    else:
        res = False
        
    return res

def TestProg():
    x = 21
    # temp = OddeSammensatt(x)
    res = GoldbachAndre(x)
    print(res)

def RunProg():
    init = 9
    while init >= 9:
        if OddeSammensatt(init):
            if not GoldbachAndre(init):
                break
            else:
                init += 2
        else:
            init += 2            
    
    return init

final_res = RunProg()
print(final_res)
    
    