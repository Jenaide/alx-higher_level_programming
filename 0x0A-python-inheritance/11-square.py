#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 7, 2023
@author: Jenaide Sibolie
"""



Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    a Square class that inherits from Rectangle.
    """
    def __init__(self, size):
        """
        init function for Square.
        
        Attributes:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        str funtion to print with/height
        Returns:
            Return width/height
        """
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)

    def area(self):
        """
        A function that calculates the area of the Square
        """
        return self.__size ** 2
