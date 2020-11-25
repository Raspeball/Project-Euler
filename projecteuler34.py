#
# Importing #
import math


def DigitFact(num):
    digit_fact_sum = 0

    for j in str(num):
        digit_fact_sum += math.factorial(int(j))

    return digit_fact_sum

total_df_sum = 0

for i in range(3, 100000):
    if i == DigitFact(i):
        total_df_sum += i
        print(i)
    else:
        continue

print(total_df_sum)
