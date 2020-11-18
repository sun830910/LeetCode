# -*- coding: utf-8 -*-

"""
Created on 2020-11-18 13:41
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def countSegments(s):
    cnt = 0
    idx = 0
    start = False
    s += " "
    while idx < len(s):
        if s[idx] != " ":
            start = True
        elif s[idx] == " " and start:
            cnt += 1
            start = False
        idx += 1
    return cnt


if __name__ == '__main__':
    s = "Hello, my name is John"
    print(countSegments(s))
    s = "    "
    print(countSegments(s))
    s = "a "
    print(countSegments(s))
    s = " a "
    print(countSegments(s))
    s = "b  a "
    print(countSegments(s))
    s = "b    a "
    print(countSegments(s))
