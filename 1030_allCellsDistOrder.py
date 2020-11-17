# -*- coding: utf-8 -*-

"""
Created on 2020-11-17 10:25
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def allCellsDistOrder(R, C, r0, c0):
    result = [(i, j) for i in range(R) for j in range(C)]
    result.sort(key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
    return result


if __name__ == '__main__':
    R = 2
    C = 3
    r0 = 1
    c0 = 2
    print(allCellsDistOrder(R, C, r0, c0))
