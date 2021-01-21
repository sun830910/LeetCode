# -*- coding: utf-8 -*-

"""
Created on 1/21/21 8:51 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def xorOperation(n, start):
    result = 0
    nums = [start + 2 * idx for idx in range(n)]
    for num in nums:
        result = result ^ num
    return result


def xorOperation2(n, start):
    result = 0
    for idx in range(n):
        result = result ^ (start + 2 * idx)
    return result


if __name__ == '__main__':
    n = 5
    start = 0
    print(xorOperation2(n, start))

    n = 4
    start = 3
    print(xorOperation2(n, start))

    n = 1
    start = 7
    print(xorOperation2(n, start))

    n = 10
    start = 5
    print(xorOperation2(n, start))
