#!/usr/bin/python3
def print_last_digit(number):
    num = 0
    absnum = abs(number)
    if absnum > 10:
        num = absnum % 10
    else:
        num = absnum
    print("{:d}".format(num), end='')
    return (num)
