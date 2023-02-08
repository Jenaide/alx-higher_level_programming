#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Jenaide Sibolie
"""



class BaseGeometry():
    """
    an Empty class
    """
    pass

    def area(self):
        """
        public instance method that calculates
        the area and Raises an exception if area
        is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates int input.
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")
