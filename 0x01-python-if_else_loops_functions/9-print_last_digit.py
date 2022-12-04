#!/usr/bin/python3
def print_last_digit(number):
    num = 0
    if number > 10:
        num = number % 10
    else:
        number = number
    return num
