# -*- coding: utf-8 -*-

"""
Created on 2020-11-16 16:30
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def strStr(haystack, needle):
    length = len(needle)
    if not haystack and not needle or length == 0:
        return 0
    if len(haystack) < length:
        return -1
    idx = 0
    while idx <= len(haystack) - length:
        if haystack[idx] == needle[0]:
            split = haystack[idx:idx + length]
            if split == needle:
                return idx
        idx += 1
    return -1


if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"
    print(strStr(haystack, needle))  # 2
    haystack = "aaaaa"
    needle = "bba"
    print(strStr(haystack, needle))  # -1
    haystack = ""
    needle = ""
    print(strStr(haystack, needle))  # 0
    haystack = ""
    needle = "a"
    print(strStr(haystack, needle))  # -1
    haystack = "a"
    needle = ""
    print(strStr(haystack, needle))  # 0
    haystack = "a"
    needle = "a"
    print(strStr(haystack, needle))  # 0
