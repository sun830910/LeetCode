# -*- coding: utf-8 -*-

"""
Created on 2020-09-03 15:29
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def findNumberIn2DArray(matrix, target):
    if len(matrix) == 0:
        return False

    height_idx = 0
    width_idx = len(matrix[0]) - 1

    while height_idx < len(matrix) and width_idx >= 0:
        if matrix[height_idx][width_idx] == target:
            return True
        if matrix[height_idx][width_idx] > target:
            width_idx -= 1
        elif matrix[height_idx][width_idx] < target:
            height_idx += 1
    return False

if __name__ == '__main__':
    matrix = [
                [1,   4,  7, 11, 15],
                [2,   5,  8, 12, 19],
                [3,   6,  9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30]
            ]
    target = 5
    print(findNumberIn2DArray(matrix, target))
    target = 20
    print(findNumberIn2DArray(matrix, target))

    matrix = []
    target = 0
    print(findNumberIn2DArray(matrix, target))
