# -*- coding: utf-8 -*-

"""
Created on 1/5/21 1:44 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def maxSubArray(nums):
    if not nums:
        return 0
    length = len(nums)
    result = [0] * length
    result[0] = nums[0]
    for idx in range(1, length):
        result[idx] = max(result[idx - 1] + nums[idx], nums[idx])
    return max(result)


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubArray(nums))
    nums = [-1]
    print(maxSubArray(nums))
    nums = [-2,1]
    print(maxSubArray(nums))