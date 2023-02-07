#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 7, 2023
@author: Jenaide Sibolie
"""



def class_to_json(obj):
    """
    a function that returns the dictionary description
    with simple data structure (list, dictionary, string,
    integer and boolean) for JSON serialization of an object.
    """
    return {key: value for (key, value) in obj.__dict__.items()
        if key in list(obj.__dict__.keys())}
