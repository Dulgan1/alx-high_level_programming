#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
strg = "Last digit of {0} is {1}"
strg2 = "and is greater than 5"
strg3 = "and is less than 6 and not 0"

num = number % 10
if number >  0:
    if num > 5:
        print(strg.format(number, num) + ' ' + strg2)
    elif num < 6 and num != 0:
        print(strg.format(number, num) + ' ' + strg3)
    else:
        print(strg.format(number, num) + ' ' + "and is 0")
else:
    number = number * -1
    num = number % 10
    num = num * -1
    number = number * -1
    print(strg.format(number, num) + ' ' + strg3)

