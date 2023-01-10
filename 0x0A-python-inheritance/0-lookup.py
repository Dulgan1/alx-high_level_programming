#!/usr/bin/python3
"""
Module 0-lookup

Contains method lookup that get list of attributes or methods of an object
"""

def lookup(obj):
    """ returns list of object's attribute and methods """
    return dir(obj)
