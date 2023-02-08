#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 7, 2023
@author: Jenaide Sibolie
"""



Rectangle = __import__('9-rectangle').Rectangle



class Square(Rectangle):
    """
    a class Square that inherits from
    rectangle.
    """
    def __init__(self, size):
        """
        init function for square.
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
