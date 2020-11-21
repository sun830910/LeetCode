# -*- coding: utf-8 -*-

"""
Created on 11/22/20 1:51 AM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def isPalindrome(x):
    x = str(x)
    left_idx = 0
    right_idx = len(x) - 1
    while right_idx >= left_idx:
        if x[right_idx] != x[left_idx]:
            return False
        right_idx -= 1
        left_idx += 1
    return True

if __name__ == '__main__':
    x = 121
    print(isPalindrome(x))
    x = -121
    print(isPalindrome(x))
    x = 10
    print(isPalindrome(x))
    x = 0
    print(isPalindrome(x))