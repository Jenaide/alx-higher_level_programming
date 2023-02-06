#!/usr/bin/python3
"""
function that returns the list of available 
attributes and methods of an object.
"""
def lookup(obj):
    """
    Returns all objects in an objects dictionary as a list.
    """
    return dir(obj)
