#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday Feb 3, 2023
@author: Jenaide Sibolie
"""



def append_write(filename="", text=""):
    """
    a function that appends a string at the end
    of a text file (UTF8) and returns the number
    of characters added.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
