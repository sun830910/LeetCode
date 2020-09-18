# -*- coding: utf-8 -*-

"""
Created on 2020-09-18 16:58
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def isPalindrome(s):
    # if s
    s = s.lower()
    left_idx = 0
    right_idx = len(s) - 1
    while left_idx < right_idx:
        if s[left_idx].isalnum() and s[right_idx].isalnum():
            if s[left_idx] == s[right_idx]:
                left_idx += 1
                right_idx -= 1
            else:
                return False
        if not s[left_idx].isalnum():
            left_idx += 1
        if not s[right_idx].isalnum():
            right_idx -= 1
    return True


if __name__ == '__main__':
    test = "A man, a plan, a canal: Panama"
    print(isPalindrome(test))  # t

    test = "race a car"
    print(isPalindrome(test))  # f

    test = " "
    print(isPalindrome(test))
    test = "    "
    print(isPalindrome(test))