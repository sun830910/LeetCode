# -*- coding: utf-8 -*-

"""
Created on 2020-09-18 17:14
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def isPerfectSquare(num):
    if num == 1:
        return True
    left = 1
    right = num

    while left < right:
        mid = left + (right - left) // 2
        if mid ** 2 == num:
            return True
        elif mid ** 2 > num:
            right = mid
        else:
            left = mid+1
    return False

if __name__ == '__main__':
    test = 16
    print(isPerfectSquare(test))

    test = 14
    print(isPerfectSquare(test))

    test = 0
    print(isPerfectSquare(test))

    test = 1
    print(isPerfectSquare(test))  # t