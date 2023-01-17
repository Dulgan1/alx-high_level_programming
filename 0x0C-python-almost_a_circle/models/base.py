#!/usr/bin/python3
"""
Module contaons class Base

Contains class atttibute __nb_object
Returns JSON rep of list dictionary
Saves JSON string of obejct to a file
Return list of instances
Saves to CSV file and loads to CSV file
More...
"""


class Base:
    """
    defines class Base

    Class Attributes:
        (int) __nb_objects
    Methods:
        __init__(self, id=None)
    Class Methods:
        save_to_file(cls, list_obj) save_to_file_csv(cls, list_obj)
        create(cls, **dictionary)
        load_from_file(cls) load_from_file_csv(cls)
    Static Methods:
        to_json_string(list_dictionaries) from_json_string(json_string)
    """
    __nb_objects = 0

   def __init__(self, id=None):
        if id is None
            Base.__nb_object += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
