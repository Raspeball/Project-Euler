from itertools import permutations

nums = [i for i in range(10)]

perms = [p for p in permutations(nums)]
perms.sort()
goal = int(1e6 - 1)
test = int(1e6)

print(perms[goal])
print(perms[test])
