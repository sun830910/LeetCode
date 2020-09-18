# -*- coding: utf-8 -*-

"""
Created on 2020-09-17 17:53
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def strStr(haystack, needle):
    sub_length = len(needle)-1
    for idx in range(len(haystack)-sub_length):
        if haystack[idx: idx+sub_length+1] == needle:
            return idx
    return -1


if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"
    print(strStr(haystack, needle))

    haystack = "aaaaa"
    needle = "bba"
    print(strStr(haystack, needle))