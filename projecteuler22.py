f = open("p022_names.txt", "r")
#
for names in f:
    name_list = names.split(",")

f.close()

name_list.sort()

for n in range(len(name_list)):
    name_list[n] = name_list[n].strip('"')

print(name_list)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def AlphaSum(name):

    sum = 0
    for i in name:
        sum += (alphabet.index(i) + 1)

    return sum

print(AlphaSum(name_list[0]))

total_name_score = 0

for n in range(len(name_list)):
    total_name_score += (AlphaSum(name_list[n])*(n + 1))

print(total_name_score)
