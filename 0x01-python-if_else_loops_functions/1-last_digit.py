#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number % 10
if number >  0:
    if num > 5:
        print("Last digit of {0} is {1} and is greater than 5".format(number, num))
    elif num < 6 and num != 0:
        print("Last digit of {0} is {1} and is less than 6 and not zero".format(number, num))
    else:
        print("Last digit of {0} is {1} and is zero".format(number, num))
else:
    number = number * (-1)
    num = number % 10
    print("Last digit of -{0} is -{1} and is less than 6 and not zero".format(number, num))

