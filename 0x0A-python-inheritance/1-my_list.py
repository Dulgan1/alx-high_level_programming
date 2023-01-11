#!/usr/bin/python3
"""
Module 1-my_list

Contains class MyList
inherits from list
"""


class MyList(list):
    """
    inherits from class list
    methods:
    print_sorted(self)
    """
    def print_sorted(self):
        """ prints list ofint all sorted in ascending order"""
        print(sorted(self))
