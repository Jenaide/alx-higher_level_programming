#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    A function that prints x elements of a list
    """
    print_1 = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            print_1 += 1
        except:
            continue
    print()
    return print_1
