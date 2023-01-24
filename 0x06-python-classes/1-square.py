#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Class Square that has attrributes. Instantiation with size
    Attributes: size (int): The size of the Square
    """
    def __init__(self, size):
        """The __init__ method of square class
        Args:
              size: (:obj: 'int'): A private instance size
        """
        self.__size = size
