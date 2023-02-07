#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 2, 2023
@author: Jenaide Sibolie
"""
import json


def from_json_string(my_str):
    """
    a function that returns an object 
    (Python data structure) represented 
    by a JSON string.
    """
    return json.loads(my_str)
