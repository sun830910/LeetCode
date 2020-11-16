# -*- coding: utf-8 -*-

"""
Created on 2020-11-16 17:54
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def reverseString(s):
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    print(reverseString(s))
    s = ["H", "a", "n", "n", "a", "h"]
    print(reverseString(s))
