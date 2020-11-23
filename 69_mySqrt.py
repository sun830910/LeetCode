# -*- coding: utf-8 -*-

"""
Created on 11/23/20 9:36 AM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def mySqrt(x):
    if x == 1:  # 这里写的不好
        return 1
    left = 0
    right = x
    while right - left > 1:
        mid = (left + right) // 2
        if mid ** 2 > x:
            right = mid
        elif mid ** 2 < x:
            left = mid
        else:
            return mid
    return left


if __name__ == '__main__':
    for val in range(10):
        print(mySqrt(val))
