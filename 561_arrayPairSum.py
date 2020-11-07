# -*- coding: utf-8 -*-

"""
Created on 2020-11-07 22:29
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def arrayPairSum(nums):
    if not nums:
        return None
    nums.sort()
    max_idx = 0
    result = 0
    while max_idx < len(nums):
        result += nums[max_idx]
        max_idx += 2
    return result


if __name__ == '__main__':
    nums = [1, 4, 3, 2]
    print(arrayPairSum(nums))
    nums = [6, 2, 6, 5, 1, 2]
    print(arrayPairSum(nums))
