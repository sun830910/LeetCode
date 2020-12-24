# -*- coding: utf-8 -*-

"""
Created on 12/24/20 4:37 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def get_ASCII_dict():
    result = dict()
    for idx in range(65, 65 + 26):
        result[chr(idx)] = idx
    print(result)


def titleToNumber(s):
    result = 0
    if not s:
        return result
    for idx in range(len(s)):
        result += (ord(s[idx]) - 64) * (26 ** (len(s) - idx - 1))
    return result


if __name__ == '__main__':
    s = 'A'
    print(titleToNumber(s))
    s = 'AA'
    print(titleToNumber(s))
    s = "AB"
    print(titleToNumber(s))
    s = 'AAA'
    print(titleToNumber(s))
    s = "ZY"
    print(titleToNumber(s))