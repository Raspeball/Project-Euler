## Problem 17 ##
#
'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out
in words, how many letters would be used?

NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters. The use of "and" when writing out
numbers is in compliance with British usage.
'''
#
#
#
# importing #
import random
#
#
#
def SpellNumberBelowHundred(num):
    # Fill and define dictionaries #
    text_ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    ones = {t+1:n for t, n in enumerate(text_ones)}

    text_tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    tens = {(t+2):n for t, n in enumerate(text_tens)}

    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    # spell number #
    # num has length 2 #
    num = str(num)

    if len(num) > 1:
        if num[0] == "1":
            spell = teens[eval(num[1])]

        else:
            if num[1] != "0":
                spell = tens[eval(num[0])] + ones[eval(num[1])]

            else:
                spell = tens[eval(num[0])]

    else:
        spell = ones[eval(num)]

    return spell
#
#

def SpellNumberBelowThousand(num):
    # num has length 3 #
    #
    # first take care of the whole hundreds #
    if num % 100 == 0:
        spell = SpellNumberBelowHundred(eval(str(num)[0])) + "hundred"

    else:
        num = str(num)
        # spell number #
        if len(num) < 3:
            spell = SpellNumberBelowHundred(eval(num))

        else:
            spell = SpellNumberBelowHundred(eval(num[0])) + "hundredand"

            if num[1] == "0":
                spell += SpellNumberBelowHundred(eval(num[2]))
            else:
                spell += SpellNumberBelowHundred(eval(num[1] + num[2]))

    return spell
#
#
def CountLetters(list_of_nums):
    count = 0
    for num in list_of_nums:
        count += len(SpellNumberBelowThousand(num))

    return count
#
#
# main program#
def main():
    res = CountLetters(list(range(1, 1000)))

    res = res + len("onethousand")

    print(res)
#
#
#
# run program #
if __name__ == '__main__':
    main()
