# -*- coding: utf-8 -*-

"""
Created on 12/6/20 2:12 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def reverseOnlyLetters(S):
    result = list(S)
    left = 0
    right = len(result) - 1
    while left < right:
        if result[left].isalpha() and result[right].isalpha():
            result[left], result[right] = result[right], result[left]
            left += 1
            right -= 1

        if not result[left].isalpha():
            left += 1
        if not result[right].isalpha():
            right -= 1
    return "".join(result)


if __name__ == '__main__':
    S = "ab-cd"
    print(reverseOnlyLetters(S))

    S = "a-bC-dEf-ghIj"
    print(reverseOnlyLetters(S))

    S = "Test1ng-Leet=code-Q!"
    print(reverseOnlyLetters(S))
