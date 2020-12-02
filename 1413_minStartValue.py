# -*- coding: utf-8 -*-

"""
Created on 12/2/20 10:40 AM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def minStartValue(nums):
    length = len(nums)
    record = [0] * length
    for idx in range(length):
        record[idx] = record[idx - 1] + nums[idx]

    min_num = min(record)
    if min_num < 1:
        start = 1 - min_num
    else:
        start = 1
    return start


if __name__ == '__main__':
    nums = [-3, 2, -3, 4, 2]
    print(minStartValue(nums))
    nums = [1, 2]
    print(minStartValue(nums))
    nums = [1, -2, -3]
    print(minStartValue(nums))