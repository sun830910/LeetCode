# -*- coding: utf-8 -*-

"""
Created on 11/20/20 4:46 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def findLUSlength(a, b):
    if a == b:
        return -1
    return max(len(a), len(b))


if __name__ == '__main__':
    a = "aba"
    b = "cdc"
    print(findLUSlength(a, b))
