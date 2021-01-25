# -*- coding: utf-8 -*-

"""
Created on 1/25/21 11:27 AM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def insertSort(arr):
    for idx in range(1, len(arr)):
        current_idx = idx - 1
        current_num = arr[idx]
        while current_idx >= 0 and current_num < arr[current_idx]:
            arr[current_idx + 1] = arr[current_idx]
            current_idx -= 1
        arr[current_idx + 1] = current_num
    return arr


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6]
    print(insertSort(arr))
