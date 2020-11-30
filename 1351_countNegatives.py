# -*- coding: utf-8 -*-

"""
Created on 11/30/20 10:34 AM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def countNegatives(grid):
    if not grid:
        return 0
    up = 0
    right = len(grid[0]) - 1
    cnt = 0
    while up < len(grid) and right >= 0:
        if grid[up][right] < 0:
            cnt += len(grid) - up
            right -= 1
            continue
        if grid[up][right] >= 0:
            up += 1
    return cnt


if __name__ == '__main__':
    grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    print(countNegatives(grid))
    grid = [[4, 3, 2, -1]]
    print(countNegatives(grid))
