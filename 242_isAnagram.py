# -*- coding: utf-8 -*-

"""
Created on 2020-11-17 14:13
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def isAnagram(s, t):
    s_length = len(s)
    t_length = len(t)
    if s_length != t_length:
        return False
    s_dict = dict()
    t_dict = dict()
    for idx in range(s_length):
        if s[idx] not in s_dict:
            s_dict.setdefault(s[idx], 1)
        else:
            s_dict[s[idx]] += 1
        if t[idx] not in t_dict:
            t_dict.setdefault(t[idx], 1)
        else:
            t_dict[t[idx]] += 1
    for key in s_dict:
        if key not in t_dict or s_dict.get(key) != t_dict.get(key):
            return False
    return True


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s, t))

    s = "rat"
    t = "car"
    print(isAnagram(s, t))
