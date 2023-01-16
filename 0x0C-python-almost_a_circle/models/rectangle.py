#!/usr/bin/python3
"""
Modeule contains class Rectangle

Inherits from class Base from model.base
"""


from model.base import Base


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
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value)
        """sets value to __height"""
        if type(value) is not int:
            raise TypeError("height must be integer")
        if type(value) is not int:
            raise ValueError("height must be >= 0")
        self.__height = value
