# -*- coding: utf-8 -*-

"""
Created on 11/20/20 4:52 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def reverseStr(s, k):
    length = len(s)
    result = ""
    for idx in range(0, length, 2 * k):
        tmp = s[idx:idx + k]
        result += tmp[::-1] + s[idx + k:idx + 2 * k]
    return result


if __name__ == '__main__':
    s = "abcdefg"
    k = 2
    print(reverseStr(s, k))  # bacdfeg
