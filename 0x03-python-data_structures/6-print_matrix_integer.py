#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    function that prints a matrix of integers
    """
    for row in matrix:
        row_length = len(row)
        for i in range(row_lenght):
            if i != row_lenght - 1:
                print("{:d}".format(row[i]), end=' ')
            else:
                print("{:d}".format(row[i]), end='')
        print()   
