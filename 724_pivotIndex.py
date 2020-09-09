# -*- coding: utf-8 -*-

"""
Created on 2020-09-09 23:01
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def pivotIndex(nums):
    if not nums:
        return -1
    total_sum = sum(nums)
    tmp_sum = 0
    for idx in range(len(nums)):
        tmp_sum += nums[idx]
        if tmp_sum - nums[idx] == total_sum - tmp_sum:
            return idx
    return -1

if __name__ == '__main__':
    nums = [1, 7, 3, 6, 5, 6]
    print(pivotIndex(nums))  # 3
    nums = [1, 2, 3]
    print(pivotIndex(nums))  # -1
    nums = []
    print(pivotIndex(nums))  # -1

    nums = [-1,-1,-1,-1,-1,0]
    print(pivotIndex(nums))  # 2
