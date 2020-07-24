# -*- coding: utf-8 -*-

"""
Created on 2020-06-24 13:59
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def countNegatives1(grid):
    result = 0
    for items in grid:
        for item in items:
            if item < 0:
                result += 1
    return result

def countNegatives2(grid):
    row_idx = 0
    col_idx = len(grid[0])-1
    result = 0
    while row_idx < len(grid) and col_idx >= 0:
        if grid[row_idx][col_idx] >= 0:
            row_idx += 1
        else:
            result += len(grid)-row_idx
            col_idx -= 1
    return result

if __name__ == '__main__':
    test1 = [[4,3,2,-1], [3,2,1,-1], [1,1,-1,-2], [-1, -1, -2, -3]] # 8
    test2 = [[3,2],[1,0]] # 0
    test3 = [[1,-1],[-1,-1]] # 3
    test4 = [[-1]]  # 1
    test5 = [[5,1,0],[-5,-5,-5]] # 3
    test6 = [[3,2],[-3,-3],[-3,-3],[-3,-3]] # 6
    print(countNegatives1(test1))
    print(countNegatives1(test2))
    print(countNegatives1(test3))
    print(countNegatives1(test4))
    print(countNegatives1(test5))
    print(countNegatives1(test6))

    print(countNegatives2(test1))
    print(countNegatives2(test2))
    print(countNegatives2(test3))
    print(countNegatives2(test4))
    print(countNegatives2(test5))
    print(countNegatives2(test6))