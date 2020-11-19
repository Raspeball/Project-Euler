#
#
pow = 5

def MaxDigitSum(num_len):
    digitsum = 0

    for i in range(num_len):
        digitsum += 9**pow

    return digitsum

#print(MaxDigitSum(9))


def DFP(num):
    sum_of_digit_powers = 0

    for i in str(num):
        sum_of_digit_powers += int(i)**pow

    return sum_of_digit_powers

DFP_sum = 0

for i in range(10, 10000000):
    if i == DFP(i):
        DFP_sum += i
        print(i)

print(DFP_sum)
