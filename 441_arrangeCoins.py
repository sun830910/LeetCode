# -*- coding: utf-8 -*-

"""
Created on 1/7/21 7:02 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def arrangeCoins(n):
    def get_sum(x):
        return (1 + x) * x >> 1

    left = 0
    right = n
    while left <= right:
        mid = (left + right) >>1
        if get_sum(mid) > n:
            right = mid - 1
        else:
            left = mid + 1
    return left - 1


if __name__ == '__main__':
    n = 1
    print(arrangeCoins(n))
    n = 5
    print(arrangeCoins(n))
    n = 8
    print(arrangeCoins(n))

    for num in range(10):
        print(num, arrangeCoins(num))
