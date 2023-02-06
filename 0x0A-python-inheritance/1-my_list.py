#!/usr/bin/python3
"""
A class that that inherits from list.
"""


class MyList(list):
    """
    class MyList inherits from list.
    """
    def print_sorted(self):
        """
        Public instance method that prints sorted list.
        """
        list_copy = self[:]
        list_copy.sort()
        print(list_copy)
