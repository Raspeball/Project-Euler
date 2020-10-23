

nums = open("projecteuler13_numbers.txt", "r")

lines = nums.readlines()

nums.close()

sum = 0

for i in range(len(lines)):
    lines[i] = int(lines[i])
    sum += lines[i]

str_sum = ""

for i in range(10):
    str_sum += str(sum)[i]

print(str_sum)
