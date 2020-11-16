# -*- coding: utf-8 -*-

"""
Created on 2020-11-16 17:22
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def isPalindrome(s):
    if not s:
        return True
    s = s.lower()
    left_idx = 0
    right_idx = len(s)-1
    while left_idx < right_idx:
        if not s[left_idx].isalnum():
            left_idx += 1
        if not s[right_idx].isalnum():
            right_idx -= 1
        if s[left_idx].isalnum() and s[right_idx].isalnum():
            if s[left_idx] == s[right_idx]:
                left_idx += 1
                right_idx -= 1
            else:
                return False
    return True

if __name__ == '__main__':
    # s = "A man, a plan, a canal: Panama"
    # print(isPalindrome(s))
    # s = "race a car"
    # print(isPalindrome(s))
    # s = ""
    # print(isPalindrome(s))
    # s = ""
    # print(isPalindrome(s))
    s = "0P"
    print(isPalindrome(s))