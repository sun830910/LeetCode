# -*- coding: utf-8 -*-

"""
Created on 12/7/20 5:12 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def minimumAbsDifference(arr):
    if not arr:
        return
    result = []
    arr.sort()
    record = dict()
    for idx in range(1, len(arr)):
        record[idx] = (arr[idx] - arr[idx - 1])
    min_value = min(record.values())
    for key in record.keys():
        if record.get(key) == min_value:
            result.append([arr[key - 1], arr[key]])
    return result


if __name__ == '__main__':
    arr = [4, 2, 1, 3]
    print(minimumAbsDifference(arr))
    arr = [1, 3, 6, 10, 15]
    print(minimumAbsDifference(arr))
    arr = [3, 8, -10, 23, 19, -4, -14, 27]
    print(minimumAbsDifference(arr))
