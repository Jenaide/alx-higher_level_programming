#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 7, 2023
@author: Jenaide Sibolie
"""
import json


def load_from_json_file(filename):
    """
    a function that creates an Object 
    from a JSON file.
    """
    with open(filename, encoding='utf-8') as file:
        return (json.loads(file.read()))
