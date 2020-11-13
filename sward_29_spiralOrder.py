# -*- coding: utf-8 -*-

"""
Created on 2020-11-13 15:23
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def spiralOrder(matrix):
    result = []
    if not matrix or not matrix[0]:
        return result
    left, top, right, bot = 0, 0, len(matrix[0]) - 1, len(matrix) - 1
    while left <= right and top <= bot:
        for idx in range(left, right + 1):
            result.append(matrix[top][idx])
        for idx in range(top + 1, bot + 1):
            result.append(matrix[idx][right])

        if left < right and top < bot:
            for idx in range(right - 1, left - 1, -1):
                result.append(matrix[bot][idx])
            for idx in range(bot - 1, top, -1):
                result.append(matrix[idx][left])
        left += 1
        top += 1
        right -= 1
        bot -= 1
    return result


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(spiralOrder(matrix))

    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(spiralOrder(matrix))

    matrix = []
    print(spiralOrder(matrix))

    matrix = [[]]
    print(spiralOrder(matrix))
