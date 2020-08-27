# -*- coding: utf-8 -*-

"""
Created on 2020-08-27 22:27
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def isUnique(astr):
    vocab_dict = dict()
    for idx in astr:
        if idx not in vocab_dict:
            vocab_dict.setdefault(idx, 1)
        else:
            return False
    return True

if __name__ == '__main__':
    s = "leetcode"
    print(isUnique(s))

    s = "abc"
    print(isUnique(s))
