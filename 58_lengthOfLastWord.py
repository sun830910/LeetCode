# -*- coding: utf-8 -*-

"""
Created on 2020-11-16 16:56
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def lengthOfLastWord(s):
    cnt = 0
    idx = len(s) -1
    while idx >= 0:
        if s[idx] == " " and cnt != 0:
            return cnt
        if s[idx] == " ":
            cnt = 0
        else:
            cnt += 1
        idx -= 1
    return cnt

if __name__ == '__main__':
    s = "Hello World"
    print(lengthOfLastWord(s))
    s = "Hello World   "
    print(lengthOfLastWord(s))