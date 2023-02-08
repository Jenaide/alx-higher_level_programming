#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 8, 2023
@author: Jenaide Sibolie
"""


Basegeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectangle class shape, inherits from 
    BaseGeometry.
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
