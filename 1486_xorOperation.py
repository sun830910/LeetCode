# -*- coding: utf-8 -*-

"""
Created on 2020-06-24 16:36
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def xorOperation(n, start):
    tmps = [start+2*idx for idx in range(n)]
    result = 0
    for tmp in tmps:
        result ^= tmp
    return result

print(xorOperation(5, 0))
print(xorOperation(4, 3))
print(xorOperation(1, 7))