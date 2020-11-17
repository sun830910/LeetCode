# -*- coding: utf-8 -*-

"""
Created on 2020-11-16 18:12
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def reverseVowels(s):
    if not s:
        return ""
    check_set = set(["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"])
    s_list = [idx for idx in s]
    left = 0
    right = len(s) - 1
    while left < right:
        if s_list[left] in check_set and s_list[right] in check_set:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        if s_list[left] not in check_set:
            left += 1
        if s_list[right] not in check_set:
            right -= 1
    return "".join(s_list)


if __name__ == '__main__':
    s = "hello"
    print(reverseVowels(s))
    s = "leetcode"
    print(reverseVowels(s))
    s = ""
    print(reverseVowels(s))
    s = "abc"
    print(reverseVowels(s))
    s = "bca"
    print(reverseVowels(s))
    s = " "
    print(reverseVowels(s))
    s = "a"
    print(reverseVowels(s))
    s = "c"
    print(reverseVowels(s))
    s = "aA"
    print(reverseVowels(s))
