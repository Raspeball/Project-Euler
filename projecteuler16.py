import math
#2**1 = 2
#2**2 = 4
#2**3 = 8
#2**4 = 16
#2**5 = 32
#2**6 = 64
# ... and so on
# Thus, we see that the period is 4
# 1000 = 4*250, so 2**1000 ends in the number 2
num = math.pow(2,1000)
#
sum = 0
for ds in str(int(num)):
    sum = sum + int(ds)
    #
#
print(sum)
