#!/usr/bin/python3
def print_last_digit(number):
    num = 0
    if number > 10 or number < -10:
        num = number % 10
    else:
        number = number
    if number > 0;
        print("{:d}".format(num))
    else:
        print("-{:d}".format(num))
