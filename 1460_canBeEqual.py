# -*- coding: utf-8 -*-

"""
Created on 12/2/20 9:57 AM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def canBeEqual(target, arr):
    record1 = dict()
    record2 = dict()
    length = len(target)
    if length != len(arr):
        return False
    for idx in range(length):
        target_num = target[idx]
        arr_num = arr[idx]
        if target_num not in record1:
            record1.setdefault(target_num, 1)
        else:
            record1[target_num] += 1
        if arr_num not in record2:
            record2.setdefault(arr_num, 1)
        else:
            record2[arr_num] += 1
    for key in record2.keys():
        if key not in record1 or record2.get(key) != record1.get(key):
            return False
    return True


if __name__ == '__main__':
    target = [1, 2, 3, 4]
    arr = [2, 4, 1, 3]
    print(canBeEqual(target, arr))
    target = [7]
    arr = [7]
    print(canBeEqual(target, arr))
    target = [1, 12]
    arr = [12, 1]
    print(canBeEqual(target, arr))
    target = [3, 7, 9]
    arr = [3, 7, 11]
    print(canBeEqual(target, arr))
    target = [1, 1, 1, 1, 1]
    arr = [1, 1, 1, 1, 1]
    print(canBeEqual(target, arr))
