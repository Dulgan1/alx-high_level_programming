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


import json
import csv


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
        """Initializing object"""
        if id is None:
            Base.__nb_object += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON representation of list dict"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(lsit_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns list dict representation of JSON"""
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves json string of all instancess to a file"""
        objs = []
        if list_objs is not None:
            for n in list_objs:
                objs.append(cls.to_dictionary(n))
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(objs))

    @classmethod
    def create(cls, **dictionary):
        """Returns instance with attributes"""
        if cls.__name__ == "Square":
           dum = cls(1)
        if cls.__name__ == "Rectangle":
           dum = cls(1, 1)
        dum.update(**dictionary)
        return dum

    @classmethod
    def load_from_file(cls):
        """Returns list of instances"""
        filename = cls.__name__ + ".json"
        l = []
        try:
            with open(filename, 'r') as f:
                instances = cls.from_json_string(f.read())
            for i, dic in enumerate(instances):
                l.append(cls.create(**instances[i]))
        except:
            pass
        return l

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves instances data to csv"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
        for n in list_objs:
            if cls.__name__ == "Rectangle":
                writer.writerow([n.id, n.width, n.height, n.x, n.y])
            if cls.__name__ == "Square":
                writer.writerow([n.id, n.size, n.x, n.y])

    @classmethod
    def load_from_file_csv(cls):
        objs = []
        filename = cls.__name__ + ".csv"
        with open(filename, 'r', newline='') as f:
            reader = reader(f)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    dic = {"id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4])}
                if cls.__name__ == "Square":
                    dic = {"id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3])}
                n = cls.create(**dic)
                objs.append(n)
        return objs
