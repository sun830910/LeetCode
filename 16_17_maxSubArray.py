# -*- coding: utf-8 -*-

"""
Created on 2020-08-24 18:57
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def maxSubArray(nums):
    length = len(nums)
    dp = [0] * length
    dp[0] = nums[0]
    for idx in range(1, len(dp)):
        dp[idx] = max(dp[idx-1] + nums[idx], nums[idx])
    return max(dp)

if __name__ == '__main__':
    test1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubArray(test1))