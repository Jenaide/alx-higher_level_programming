#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13, 2023
@author: Jenaide Sibolie
"""
from models.base import Base


class Rectangle(Base):
    """
    A Rectangle class that inherits from Base.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor for Rectangle

        Attr:
            width (int): Private attribute for the width of the Rectangle
            height (int): Private attribute for the height of the Rectangle
            x (int): Private attribute for x value of the Rectangle
            y (int): Private attribute for y value of the Rectangle
            id (int): Private attribute id inherits from Base
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @x.setter
    def x(self, value):
        """
        the setter method for x value

        Attr:
           value (int): check if the value is an int and greater
           than 0.
        """
        if type(value) != int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    def area(self):
        """
        Calculates the area of the Rectangle class

        Returns:
            The area of the Retangle
        """
        return self.width * self.height

    def display(self):
        """
        Prints in stdout with the # char Retangle
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(' ', end='')
            for j in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """
        __str__ method for Retangle class
        
        Return:
            The string: [class_name] (id) x/y - width/height.
        """
        method = "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                  self.id, self.x self.y,
                                                  self.width, self.height)
        return method

    def update(self, *args, **kwargs):
        """
        update the retangle class
       
        Attr:
            args (list): input arguments that updates retangle class
            kwargs (dict): input arguments that updates retangle class
        """
        if args is not None and len(args) != 0:
            for i, ar in enumerate(args):
                if i == 0:
                    self.id = ar
                elif i == 1:
                    self.width = ar
                elif i == 2:
                    self.height = ar
                elif i == 3:
                    self.x = ar
                elif i == 4:
                    self.y = ar

        elif kwargs is not None and len(kwargs) != 0:
            for (key, value) in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        creates a dictionary representation of a Rectangle.
        
        return:
            dictionary representation
        """
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height,
                'width': self.width}
