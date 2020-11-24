# Project Eueler #40 #

#
#

# Initialize #
frac_part = ""

# Create complete string #
for i in range(1, 1000001):
    frac_part += str(i)

#print(frac_part)

dig_prod = 1

for i in range(0,6):
    t = int(frac_part[(10**i)-1])
    dig_prod = dig_prod*t

print(dig_prod)
