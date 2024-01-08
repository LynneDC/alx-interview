#!/usr/bin/python3
"""
Pascal triangle module
"""


def pascal_triangle(n):
    """ Create a list of lists that represent integers
    representing Pascal's Triangle
    """
    tri = []

    # Check if n is not int or less than 0
    if type(n) is not int or n <= 0:
        return tri

    # Iterate through the list of lists
    for i in range(n):
        a = []

        # Iterate the second list of lists
        for j in range(i + 1):
            if j == 0 or j == i:
                a.append(1)
            elif i > 0 and j > 0:
                a.append(tri[i - 1][j - 1] + tri[i - 1][j])

        tri.append(a)

    return tri
