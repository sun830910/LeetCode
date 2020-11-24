# -*- coding: utf-8 -*-

"""
Created on 11/23/20 9:58 AM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def climbStairs(n):
    result = dict()
    result[1] = 1
    result[2] = 2
    for idx in range(3, n + 1):
        result[idx] = result[idx - 1] + result[idx - 2]
    return result[n]


if __name__ == '__main__':
    n = 2
    print(climbStairs(n))
