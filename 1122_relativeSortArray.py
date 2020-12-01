# -*- coding: utf-8 -*-

"""
Created on 12/1/20 4:57 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def relativeSortArray(arr1, arr2):
    result = []
    if not arr1 or not arr2:
        return result
    record1 = dict()
    for val in arr1:
        if val not in record1:
            record1.setdefault(val, 1)
        else:
            record1[val] += 1
    for num in arr2:
        if num in record1:
            result += [num] * record1.get(num)
            record1.pop(num)
    sorted_key = sorted(record1.keys())
    for key in sorted_key:
        result += [key] * record1.get(key)
    return result


if __name__ == '__main__':
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    print(relativeSortArray(arr1, arr2))  # [2,2,2,1,4,3,3,9,6,7,19]
