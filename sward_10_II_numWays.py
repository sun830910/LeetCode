# -*- coding: utf-8 -*-

"""
Created on 1/20/21 5:58 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def numWays(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a % 1000000007


if __name__ == '__main__':
    n = 1
    print(numWays(n))
    n = 2
    print(numWays(n))
    n = 3
    print(numWays(n))
    n = 7
    print(numWays(n))
