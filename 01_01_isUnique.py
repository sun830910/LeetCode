# -*- coding: utf-8 -*-

"""
Created on 2020-11-13 14:55
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def isUnique(astr):
    if len(set(astr)) != len(astr):
        return False
    return True


if __name__ == '__main__':
    s = "leetcode"
    print(isUnique(s))
    s = "abc"
    print(isUnique(s))
