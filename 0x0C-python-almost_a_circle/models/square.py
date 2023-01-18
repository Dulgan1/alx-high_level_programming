#!/usr/bin/python3
"""
Module contains Square class

Inherits from class Rectangle of model.rectangle
Overloads __str__ method
Returns area of object Square
Updates objects attributes
Objects data is saved to dictionary
"""


from models.rectangle import Rectangle


class Square:
    """Defines the class Square

    Inherits attribute:
        __y, __x, __width, __height, id
    Methods:
        size(self), size(self, value), __str__(self)
        update(self, *args, **kwargs),
        __init__(self, size, x=0, y=0, id=None)
        to_dictionary(self)
    Also inherits methods of calss Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing method"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """gets size"""
        return self.size

    @size.setter
    def size(self, value):
        """sets value to width, height"""
        self.width = value
        self.height = value

    def __str__(self):
        """Overloads __str__ with [Square] (<id>) <x>/<y> - <size>"""
        f_str = "[{:s}] ({:d})".format(self.__class__.__name__, self.id)
        s_str = "{:d}/{:d} - {:d}".format(self.x, self.y, self.size)
        return f_str + " " + s_str

    def update(self, *args, **kwargs):
        if args:
            for k, v in enumerate(args):
                if k == 0:
                    self.id = v
                elif k == 1:
                    self.size = v
                elif k == 2:
                    self.x = v
                else:
                    self.y = v
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Returns dictionary representation of class object"""
        d = {}
        d["id"] = self.id
        d["size"] = self.size
        d["x"] = self.x
        d["y"] = self.y
        return d
