#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 8, 2023
@author: Jenaide Sibolie
"""



BaseGeometry = __import__('7-rectangle').BaseGeometry


class Retangle(BaseGeometry):
    """
    A Rectangle class that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        init function for rectangle

        Attributes:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        str funtion for rectangle
        Returns:
            Return width/height
        """
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)

    def area(self):
        """
        Calculates the area of the rectangle
        Return:
           The area of the rectangle
        """
        return self.__width * self.__height