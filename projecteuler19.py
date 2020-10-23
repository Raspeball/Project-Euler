import math


def IsLeap(year):

    if year % 4 == 0:
        if year % 400 == 0:
            return True
        else:
            if year % 100 == 0:
                return False
            else:
                return True
    else:
        return False

#test = 2000
#print(IsLeap(test))


days = 2  # 1. jan 1900 was a monday, 1. jan 1901 was tuesday
sunday_first = 0

year = 1901
# start_day = 2

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while year < 2001:
    if IsLeap(year):
        month_days[1] = 29
    else:
        month_days[1] = 28

    for m in month_days:
        days += m
        if days % 7 == 0:
            sunday_first += 1
        #end_day = start_day + (m % 7) - 1
        #if end_day == 6:
        #    sunday_first += 1

        #start_day = end_day
        #if start_day > 7:
        #    start_day = start_day % 7



    year += 1

print(sunday_first)
