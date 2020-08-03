# -*- coding: utf-8 -*-

"""
Created on 2020-08-03 22:47
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def findMaxAverage(nums, k):
    length = len(nums)
    dp = [0] * (length - k +1)
    dp[0] = sum(nums[:k]) / k
    for idx in range(1, length-k+1):
        dp[idx] = dp[idx-1] if nums[idx-1] >= nums[idx+k-1] else sum(nums[idx:idx+k])/k
    return max(dp)

def findMaxAverage2(nums, k):
    length = len(nums)
    numSum = [0] * length
    numSum[0] = nums[0]
    for idx in range(1, length):
        numSum[idx] = numSum[idx-1] + nums[idx]
    result = numSum[k-1]
    for idx in range(k, length):
        result = max(result, numSum[idx] - numSum[idx-k])

    return result/k

def findMaxAverage(nums, k):
    length = len(nums)
    numSum = sum(nums[:k])
    result = numSum
    for idx in range(1, length-k+1):
        numSum = numSum + nums[idx+k-1] - nums[idx-1]
        result = max(result, numSum)
    return result/k

nums = [1,12, -5, -6, 50, 3]
k = 4
print(findMaxAverage(nums, k))