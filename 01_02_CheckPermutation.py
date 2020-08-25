# -*- coding: utf-8 -*-

"""
Created on 2020-08-24 20:31
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def CheckPermutation(s1, s2):
    s1_dict = dict()
    s2_dict = dict()
    for s1_idx in s1:
        if s1_idx not in s1_dict:
            s1_dict.setdefault(s1_idx, 1)
        else:
            s1_dict[s1_idx] += 1
    for s2_idx in s2:
        if s2_idx not in s2_dict:
            s2_dict.setdefault(s2_idx, 1)
        else:
            s2_dict[s2_idx] += 1
    return s1_dict == s2_dict

if __name__ == '__main__':
    s1 = "abc"
    s2 = "bca"
    print(CheckPermutation(s1, s2))

    s1 = "abc"
    s2 = "bad"
    print(CheckPermutation(s1, s2))

    s1 = "a"
    s2 = "ab"
    print(CheckPermutation(s1, s2))

    s1 = "asvnpzurz"
    s2 = "urzsapzvn"
    print(CheckPermutation(s1, s2))

