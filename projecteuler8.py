#
#
f = open("projecteuler8_string.txt","r")
n = f.read()#the number in question

n_list = []

for i in range(len(n)):
    if n[i] == '\n':
        continue
    else:
        n_list.append(float(n[i]))
#
#print(n_list)
def adjacent_prod(num_list,series):
    startval = 0
    prod = 0
    for i in range(len(num_list)-series):#subtract series bco list out of bounds
        temp_prod = 1#NB, can not be set to 0 for obvious reasons
        for j in range(series):
            temp_prod = temp_prod*num_list[i+j]
            #
        if temp_prod > prod:
            prod = temp_prod
            startval = i
        else:
            continue
            #
        #
    #
    return(prod)
    #
#
#
pe8_sol = adjacent_prod(n_list,13)
print(pe8_sol)
