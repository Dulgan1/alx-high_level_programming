#!/usr/bin/python3
def print_last_digit(number):
    num = 0
    if abs(number) > 10:
        num = number % 10
    else:
        num = number
    print("{:d}".format(num))
