# -*- coding: utf-8 -*-

"""
Created on 1/12/21 8:33 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def printNumbers(n):
    result = []
    if n <= 0:
        return result
    num = int("9" * n)
    for idx in range(1, num + 1):
        result.append(idx)
    return result


if __name__ == '__main__':
    n = 0
    print(printNumbers(n))

    n = 1
    print(printNumbers(n))

    n = 2
    print(printNumbers(n))
