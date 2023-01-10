#!/usr/bin/python3
"""
Module 2-is_same_class

Contains method is_same_class
returns true if the passed objects is instance of specified class
"""

def is_same_class(obj, a_class):
    """ Return:
    True if object is exactly an instance of the class
    """
    return type(obj) == a_class
