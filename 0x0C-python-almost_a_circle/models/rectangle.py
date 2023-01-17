#!/usr/bin/python3
"""
Modeule contains class Rectangle

Inherits from class Base from model.base
Displays class object in #s
Converts class data to dictionary
Overloads __str__ method
Updates objects attributes
Returns area of object Rectangle
"""


from models.base import Base


class Rectangle(Base):
    """defines class Rectangle which inherits from Base class

    inherits attribute id of Base
    Attributes:
        __x  __y __width __height
    Methods:
        __init__(self, width, height, x=0, y=0)
    Getter methods:
        x(self) gets __x
        y(self) gets __y
        width(self) gets __width
        height(self) gets __height
    Setter Methods:
        x(self, value) sets value to __x
        y(self, value) sets value to __y
        width(self, value) sets value to __width
        height(self, value) sets value to __height
    More...
    """

    def __init__(self, width, height, x=0, y=0):
        """Initializing method"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def x(self):
        """x getter"""
        return self.__x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @x.setter
    def x(self, value):
        """sets value to __x"""
        if type(value) is not int:
            raise TypeError("x  must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """sets value to __y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @width.setter
    def width(self, value):
        """sets value to __width"""
        if type(value) is not int:
            raise TypeError("width must be integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """sets value to __height"""
        if type(value) is not int:
            raise TypeError("height must be integer")
        if value <= 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """Displays the representation of class with #'s"""
        print("\n" * self.__y)
        for i in range(0, self.__height):
            print(" " * self.__x)
            for i in range(0, self.__width):
                if i != self.__width - 1:
                    print("#", end="")
                else:
                    print("#")

    def __str__(self):
        """Overrides the __str__ method"""
        f_str = "[{:s}] ({:d})".format(self.__class__.__name__, self.id)
        s_str = "{:d}/{:d} -".format(self.__x, self.__y)
        t_str = "{:d}/{:d}".format(self.__width, self.__height)
        return f_str + " " + s_str + " " + t_str

    def update(self, *args, **kwargs):
        """updates object attributes"""
        if args:
            for k, v in enumerate(args):
                if k == 0:
                    self.id = v
                elif k == 1:
                    self.__width = v
                elif k == 2:
                    self.__height = v
                elif k == 3:
                    self.__x = v
                else:
                    self.__y = v

        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.__width = kwargs["width"]
            if "height" in kwargs:
                self.__height = kwargs["height"]
            if "x" in kwargs:
                self.__x = kwargs["x"]
            if "y" in kwargs:
                self.__y = kwargs["y"]

    def to_dictionary(self):
        """Returns dictionary representation of class"""
        d = {}
        d["id"] = self.id
        d["width"] = self.width
        d["height"] = self.height
        d["x"] = self.x
        d["y"] = self.y
        return d
