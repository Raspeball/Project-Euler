import math

def ProbDistDisk(red, blue):
    tot = red + blue
    
    P_bb = (blue/tot)*((blue-1)/(tot-1))
    
    if P_bb == 0.5:
        return blue
    else:
        return 0
    

def RunProg(disks):
    red = disks/2
    blue = disks/2
    res = 0
    
    while res == 0:
        blue_disks = ProbDistDisk(red, blue)
        res = blue_disks
        
        