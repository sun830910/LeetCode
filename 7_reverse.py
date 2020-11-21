# -*- coding: utf-8 -*-

"""
Created on 11/21/20 11:38 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def reverse(x):
    if x >= 0:
        x = int(str(x)[::-1])
    else:
        x = str(x)[1:]
        x = -1 * int(x[::-1])
    if -(2 ** 31) < x < 2 ** 31:
        return x
    return 0


if __name__ == '__main__':
    x = 123
    print(reverse(x))
    x = 120
    print(reverse(x))
    x = -123
    print(reverse(x))
    x = 0
    print(reverse(x))
