# -*- coding: utf-8 -*-

"""
Created on 2020-11-11 11:17
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def missingNumber(nums):
    if not nums or len(nums) == 0:
        return
    nums_set = set(nums)
    for idx in range(len(nums) + 1):
        if idx not in nums_set:
            return idx


if __name__ == '__main__':
    nums = [3, 0, 1]
    print(missingNumber(nums))
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(missingNumber(nums))
    nums = []
    print(missingNumber(nums))
    nums = [0]
    print(missingNumber(nums))
