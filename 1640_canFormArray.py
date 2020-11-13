# -*- coding: utf-8 -*-

"""
Created on 2020-11-13 17:39
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def canFormArray(arr, pieces):
    record = dict()
    for idx, piece in enumerate(pieces):
        if len(piece) >= 1:
            record.setdefault(piece[0], idx)
    result = []
    for idx in arr:
        if idx in record:
            result += pieces[record.get(idx)]
    return result == arr


if __name__ == '__main__':
    arr = [85]
    pieces = [[85]]
    print(canFormArray(arr, pieces))

    arr = [15, 88]
    pieces = [[88], [15]]
    print(canFormArray(arr, pieces))

    arr = [1, 3, 5, 7]
    pieces = [[2, 4, 6, 8]]
    print(canFormArray(arr, pieces))

    arr = [1, 3]
    pieces = [[], [1], [3]]
    print(canFormArray(arr, pieces))
