# -*- coding: utf-8 -*-

"""
Created on 2020-09-06 22:11
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def diagonalSum(mat):
    res = 0
    for idx in range(len(mat)):
        res += mat[idx][idx]
        res += mat[idx][len(mat)-idx-1]
    if len(mat) % 2 == 1:
        res -= mat[idx//2][idx//2]
    return res

if __name__ == '__main__':
    mat = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
    print(diagonalSum(mat))
    mat = [[1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1]]
    print(diagonalSum(mat))
    mat = [[5]]
    print(diagonalSum(mat))
