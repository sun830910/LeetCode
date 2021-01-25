# -*- coding: utf-8 -*-

"""
Created on 1/25/21 10:55 AM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def largestAltitude(gain):
    length = len(gain)
    arr = [0] * (length + 1)
    max_num = 0
    for idx in range(1, length + 1):
        arr[idx] = arr[idx - 1] + gain[idx - 1]
        if arr[idx] > max_num:
            max_num = arr[idx]
    return max_num


if __name__ == '__main__':
    gain = [-5, 1, 5, 0, -7]
    print(largestAltitude(gain))
    gain = [-4, -3, -2, -1, 4, 3, 2]
    print(largestAltitude(gain))
    gain = []
    print(largestAltitude(gain))
