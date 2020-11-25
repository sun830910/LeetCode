# -*- coding: utf-8 -*-

"""
Created on 11/25/20 6:13 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def isPerfectSquare(num):
    left = 0
    right = num
    while left <= right:
        mid = (left + right) // 2
        current = mid ** 2
        if current == num:
            return True
        elif current < num:
            left = mid + 1
        else:
            right = mid - 1
    return False


if __name__ == '__main__':
    num = 16
    print(isPerfectSquare(num))

    num = 0
    print(isPerfectSquare(num))

    num = 1
    print(isPerfectSquare(num))

    num = 14
    print(isPerfectSquare(num))
