# -*- coding: utf-8 -*-

"""
Created on 12/7/20 2:37 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def checkIfExist(arr):
    if not arr:
        return
    record = dict()
    for idx, num in enumerate(arr):
        if num * 2 not in record and num / 2 not in record:
            record.setdefault(num, idx)
        else:
            return True
    return False


if __name__ == '__main__':
    arr = [10, 2, 5, 3]
    print(checkIfExist(arr))
    arr = [7, 1, 14, 11]
    print(checkIfExist(arr))
    arr = [3, 1, 7, 11]
    print(checkIfExist(arr))
