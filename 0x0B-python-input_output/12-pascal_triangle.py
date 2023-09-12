#!/usr/bin/python3
"""
This module contains a function that generates Pascal's triangle
up to `n` levels deep.
"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal’s triangle of n.

    Args:
        n (int): The number of levels deep to generate the triangle.

    Returns:
        List of lists of integers: Representing Pascal’s triangle.

    Examples:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, len(triangle[i-1])):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
