# -*- coding: utf-8 -*-

"""
Created on 2020-09-12 21:29
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def mySqrt(x):
    left, right = 0, x+1
    while left < right:
        mid = left + (right-left)//2
        if mid ** 2 == x:
            return mid
        if mid ** 2 < x:
            left = mid + 1
        else:
            right = mid
    return left - 1

if __name__ == '__main__':
    x = 4
    print(mySqrt(x))
