#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue FEb 7 , 2023
@author: Jenaide Sibolie
"""
import json


def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object to a text file,
    using a JSON representation.
    """
    with open(filename, 'x', encoding='utf-8') as file:
        return file.write(json.dumps(my_obj))
