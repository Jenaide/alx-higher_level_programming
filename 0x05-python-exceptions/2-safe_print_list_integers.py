#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    A function that prints the first x elements
    of a list and only integers.
    """
    list_0 = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i], end="")
            list_0 += 1
        except (ValueError, TypeError):
            continue
    print()
    return list_0
