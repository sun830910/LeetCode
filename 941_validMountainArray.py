# -*- coding: utf-8 -*-

"""
Created on 12/1/20 3:11 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def validMountainArray(arr):
    if not arr:
        return
    if len(arr) < 3:
        return False
    if arr[0] > arr[1]:
        return False
    up_flag = True
    for idx in range(1, len(arr)):
        if up_flag and arr[idx] <= arr[idx-1]:
            up_flag = False
        if not up_flag and arr[idx] >= arr[idx-1]:
            return False
    if up_flag:
        return False
    else:
        return True



if __name__ == '__main__':
    arr = [2, 1]
    print(validMountainArray(arr))  # F
    arr = [3, 5, 5]
    print(validMountainArray(arr))  # F
    arr = [0, 3, 2, 1]
    print(validMountainArray(arr))  # T
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(validMountainArray(arr))  # F