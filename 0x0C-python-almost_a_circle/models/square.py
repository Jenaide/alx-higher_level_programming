#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12, 2023
@author: Jenaide Sibolie
"""
from models.rectangle import Retangle


class Square(Retangle):
    """
    a square class that inherits from retangle class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        class constructor for Square

        Attr:
            size (int): size of the square
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @size.setter
    def size(self, value):
        """
        setter method for the size value

        Attr:
            value (int): value that checks if it is an int and greater
            than 0.
        """
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.width = value

    def update(self, *args, **kwargs):
        """
        Updates Square class

        Attr:
            args (list): input arguments that updates rectangle class
            kwargs (dict): input arguments that updates rectangle class
        """
        if args is not None and len(args) != 0:
            for i, ar in enumerate(args):
                if i == 0:
                    self.id = ar
                elif i == 1:
                    self.size = ar
                elif i == 2:
                    self.x = ar
                elif i == 3:
                    self.y = ar

        elif kwargs is not None and len(kwargs) != 0:
            for (key, value) in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Creates a dictionary representation for Square attributes.

        Return:
           A dictionary representation
        """
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height,
                'width': self.width}


if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dictionary = Base.to_json_string([dictionary])
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))
