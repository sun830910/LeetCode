# -*- coding: utf-8 -*-

"""
Created on 1/5/21 3:48 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def waysToStep(n):
    a, b, c = 4, 2, 1
    if n < 3:
        return n
    if n == 3:
        return 4  # (111/12/21/3)
    for i in range(n - 3):
        a, b, c = (a + b + c) % 1000000007, a, b
    return a


if __name__ == '__main__':
    n = 10
    print(waysToStep(n))
