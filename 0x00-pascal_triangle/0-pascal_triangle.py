#!/usr/bin/python3
"""
pascal triangle module
"""

def pascal_triangle(n):
    """ Create a list of list that reprisent int
    that represent the pascal triangle 
    """
    tri = []
    #check if n is not int or less than 0
    if type(n) is not int or n <= 0:
        return tri
    #iterate through the list of list
    for i in range(n):
        a = []
        #interate the second list of lists
        for j in range (i + 1):
            if j == 0 or j == i:
                a.append(1)
            elif i > 0 and j > 0:
                a.append(tri[i -1][j -1] + tri[i -1][j])
        tri.append(a)
    return tri  
                        
