# -*- coding: utf-8 -*-

"""
Created on 11/27/20 3:56 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def sumOddLengthSubarrays(arr):
    window_size = 1
    result = 0
    while window_size <= len(arr):
        for idx in range(len(arr) - window_size + 1):
            result += sum(arr[idx:idx + window_size])
        window_size += 2
    return result


if __name__ == '__main__':
    arr = [1, 4, 2, 5, 3]
    print(sumOddLengthSubarrays(arr))
