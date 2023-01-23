#!/usr/bin/python3
def safe_print_division(a, b):
    """
    A function that divides 2
    integers and prints the results.
    """
    try:
        div = a / b
    except:
        div = None
    finally:
        print("Inside result: {}".format(div))
    return div
