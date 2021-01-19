# -*- coding: utf-8 -*-

"""
Created on 1/19/21 10:49 AM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def hammingWeight(n):
    result = 0
    while n:
        result += n & 1
        n >>= 1
    return result


if __name__ == '__main__':
    n = 0b00000000000000000000000000001011
    print(hammingWeight(n))
    n = 0b00000000000000000000000010000000
    print(hammingWeight(n))
