# -*- coding: utf-8 -*-

"""
Created on 2020-11-11 14:39
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def maxSubArray(nums):
    if not nums or len(nums) == 0:
        return
    result = [0] * len(nums)
    result[0] = nums[0]
    for idx in range(1, len(nums)):
        result[idx] = max(result[idx - 1] + nums[idx], nums[idx])
    return max(result)


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubArray(nums))
