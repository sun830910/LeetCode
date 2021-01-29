# -*- coding: utf-8 -*-

"""
Created on 1/29/21 4:42 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def kWeakestRows(mat, k):
    result = []
    if not mat:
        return result
    record = dict()

    def helper(arr):
        cnt = 0
        arr_length = len(arr)
        if arr_length == 0:
            return cnt
        arr_idx = 0
        while arr_idx < arr_length:
            if arr[arr_idx] == 1:
                cnt += 1
                arr_idx += 1
            else:
                return cnt
        return cnt

    for idx in range(len(mat)):
        record[idx] = helper(mat[idx])

    temp = sorted(record.items(), key=lambda x: x[1])
    for idx in range(k):
        result.append(temp[idx][0])
    return result


if __name__ == '__main__':
    mat = [[1, 1, 0, 0, 0],
           [1, 1, 1, 1, 0],
           [1, 0, 0, 0, 0],
           [1, 1, 0, 0, 0],
           [1, 1, 1, 1, 1]],
    k = 3
    print(kWeakestRows(mat, k))

    mat = [[1, 0, 0, 0],
           [1, 1, 1, 1],
           [1, 0, 0, 0],
           [1, 0, 0, 0]],
    k = 2
    print(kWeakestRows(mat, k))
