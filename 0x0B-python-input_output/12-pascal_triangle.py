#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 7, 2023
@author: Jenaide Sibolie
"""



def pascal_triangle(n):
    """
    a function that creates a pascal triangle.
    """
    pascal = []
    triangle = []
    
    for i in range(int(n)):
        new = pascal[:]
        new.append(1)
        post = len(pascal)
        for i in range(1, post):
            new[i] = pascal[i - 1] + pascal[i]
        pascal = new[:]
        triangle.append(pascal)
    return triangle
