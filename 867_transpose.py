# -*- coding: utf-8 -*-

"""
Created on 2020-11-14 11:10
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def transpose(A):
    if not A or not A[0]:
        return []
    height = len(A)
    width = len(A[0])
    result = [[0 for _ in range(height)] for _ in range(width)]
    for height_idx in range(height):
        for width_idx in range(width):
            num = A[height_idx][width_idx]
            if height_idx == width_idx:
                result[height_idx][width_idx] = num
            else:
                result[width_idx][height_idx] = num
    return result


if __name__ == '__main__':
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # [[1,4,7],[2,5,8],[3,6,9]]
    print(transpose(A))

    A = [[1, 2, 3], [4, 5, 6]]  # [[1,4],[2,5],[3,6]]
    print(transpose(A))
