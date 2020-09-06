# -*- coding: utf-8 -*-

"""
Created on 2020-09-06 22:56
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def findSpecialInteger(arr):
    num_cnt = dict()
    target = len(arr) // 4
    print(target)
    for num in arr:
        if num not in num_cnt:
            num_cnt.setdefault(num, 1)
        else:
            num_cnt[num] += 1
        if num_cnt[num] > target:
            return num


if __name__ == '__main__':
    arr = [1, 2, 2, 6, 6, 6, 6, 7, 10]
    print(findSpecialInteger(arr))