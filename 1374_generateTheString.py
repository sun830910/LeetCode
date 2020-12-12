# -*- coding: utf-8 -*-

"""
Created on 12/12/20 5:06 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def generateTheString(n):
    if n == 0:
        return ""
    if n & 1:
        return "a" * n
    else:
        return "a" * (n-1) + "b"


if __name__ == '__main__':
    for n in range(20):
        print(n)
        print(generateTheString(n))
        print("-" * 30)
