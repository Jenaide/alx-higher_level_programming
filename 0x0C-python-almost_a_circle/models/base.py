#!/usr/bin/python3
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
        if id is not None:
            self.id = id
        else:
            Base.__nd_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        creates a json string representation for base class

        Attr:
           list_dictionaries (json):a json list of dictionaries

        Return:
            JSON string representation
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
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
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        returns a list of a json string representation

        Attr:
           json_string (string): json obj

        Return:
            json object to dictionary
        """
        if json_string is None or json_string == "[]":
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
        if dictionary and dictionary != {}:
            if cls.__name__ == "Retangle":
                dummy = cls(1, 1)
            else:
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
        file_name = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
