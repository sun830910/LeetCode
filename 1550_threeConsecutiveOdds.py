# -*- coding: utf-8 -*-

"""
Created on 11/27/20 4:05 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def threeConsecutiveOdds(arr):
    if not arr or len(arr) < 3:
        return False
    idx = 1
    while idx < len(arr) - 1:
        if arr[idx] % 2 != 1:
            idx += 2
            continue
        if arr[idx - 1] % 2 == 1 and arr[idx] % 2 == 1 and arr[idx + 1] % 2 == 1:
            return True
        idx += 1
    return False


if __name__ == '__main__':
    # arr = [2, 6, 4, 1]
    # print(threeConsecutiveOdds(arr))  # F
    # arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]
    # print(threeConsecutiveOdds(arr))  # T
    # arr = [1, 3, 4]
    # print(threeConsecutiveOdds(arr))  # F
    # arr = [4, 1, 3, 5]
    # print(threeConsecutiveOdds(arr))  # T
    arr = [1, 2, 1, 1]
    print(threeConsecutiveOdds(arr))
