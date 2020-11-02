# -*- coding: utf-8 -*-

"""
Created on 2020-11-02 19:36
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def maxSubArray(nums):
    if not nums:
        return
    maxArr = [0] * len(nums)
    maxArr[0] = nums[0]
    for idx in range(1, len(nums)):
        maxArr[idx] = max(nums[idx], maxArr[idx-1] + nums[idx])
    return max(maxArr)

if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubArray(nums))