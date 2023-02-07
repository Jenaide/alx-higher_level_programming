#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 7, 2023
@author: Jenaide Sibolie
"""
import json


def to_json_string(my_obj):
    """
    a function that returns the JSON 
    representation of an object (string).
    """
    return json.dumps(my_obj)
