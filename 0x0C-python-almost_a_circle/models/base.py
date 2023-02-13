#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@author: Jenaide Sibolie

"""
import json


class Base:
    """
    Base class
    
    Attributes:
        _nb_objects (int): Private class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor

        Atrributes:
            id (int): An integer input for id
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        creates a json string representation for base class

        Attr:
           list_dictionaries (json):a json list of dictionaries

        Return:
            JSON string representation
        """
        if list_dictionaries is None or not list_dictionaries:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes a json string representation of list_objs to a file.

        Attr:
           list_objs (list): obj list to be saved

        Return:
            json obj to be save in a file.
        """
        file_name = cls.__name__ + ".json"
        string = []
        if list_objs is not None:
            for i in list_objs:
                string.append(cls.to_dictionary(i))
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(cls.to_json_string(string))

    @staticmethod
    def from_json_string(json_string):
        """
        returns a list of a json string representation

        Attr:
           json_string (string): json obj

        Return:
            json object to dictionary
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with ll attributes already set

        Attr:
            dictionary (dict): outdated dictionary

        Return:
           an instance with all attributes already set
        """
        if cls.__name__ == "Retangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances

        Return:
            A list of instances
        """
        file_name = cls.__name__ + ".json"
        json_obj = []
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                json_obj = cls.from_json_string(file.read())
            for key, value in enumerate(json_obj):
                json_obj[key] = cls.create(**json_obj[key])
        except:
            pass
        return json_obj
