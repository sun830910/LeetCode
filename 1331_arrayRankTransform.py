# -*- coding: utf-8 -*-

"""
Created on 11/28/20 11:00 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


# 超时
# def arrayRankTransform(arr):
#     result = []
#     if not arr:
#         return result
#     set_arr = sorted(set(arr))
#     for idx in arr:
#         result.append(set_arr.index(idx) + 1)
#     return result


def arrayRankTransform(arr):
    result = []
    if not arr:
        return result
    sorted_arr = sorted(list(set(arr)))
    hash_map = {}
    for idx, val in enumerate(sorted_arr):
        hash_map[val] = idx + 1
    return [hash_map.get(arr_idx) for arr_idx in arr]


if __name__ == '__main__':
    arr = [40, 10, 20, 30]
    print(arrayRankTransform(arr))
    arr = [100, 100, 100]
    print(arrayRankTransform(arr))
    arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
    print(arrayRankTransform(arr))
