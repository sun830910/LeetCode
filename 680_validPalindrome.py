# -*- coding: utf-8 -*-

"""
Created on 11/26/20 9:29 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

# 20%
def validPalindrome(s):
    def check(sentence):
        left = 0
        right = len(sentence) - 1
        while left < right:
            if sentence[left] != sentence[right]:
                return False
            left += 1
            right -= 1
        return True

    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return check(s[:left] + s[left + 1:]) or check(s[:right] + s[right + 1:])
        left += 1
        right -= 1
    return True


if __name__ == '__main__':
    s = "aba"
    print(validPalindrome(s))
    s = "abca"
    print(validPalindrome(s))
    s = "aabca"
    print(validPalindrome(s))
