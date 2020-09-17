# -*- coding: utf-8 -*-

"""
Created on 2020-09-17 17:18
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def isPalindrome(x):
    if x < 0:
        return False
    x_str = str(x)
    left_idx, right_idx = 0, len(x_str)-1
    while left_idx < right_idx:
        if x_str[left_idx] == x_str[right_idx]:
            left_idx += 1
            right_idx -= 1
        else:
            return False
    return True


if __name__ == '__main__':
    test = 121
    print(isPalindrome(test))
    test = -121
    print(isPalindrome(test))