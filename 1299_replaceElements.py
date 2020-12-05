# -*- coding: utf-8 -*-

"""
Created on 12/5/20 11:04 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def replaceElements(arr):
    if not arr:
        return
    result = [0] * len(arr)
    idx = 0
    while idx < len(result) - 1:
        result[idx] = max(arr[idx + 1:])
        idx += 1
    result[-1] = -1
    return result


if __name__ == '__main__':
    arr = [17, 18, 5, 4, 6, 1]
    print(replaceElements(arr))
