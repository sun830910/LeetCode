# -*- coding: utf-8 -*-

"""
Created on 2020-11-06 17:39
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


# def findMaxAverage(nums, k):
#     if not nums or len(nums) < 0:
#         return None
#     recode = [-float("inf")] * (len(nums) - k + 1)
#     for idx in range(len(recode)):
#         recode[idx] = sum(nums[idx:idx + k])  # 每次都使用sum的算法过慢
#     return max(recode) / k

def findMaxAverage(nums, k):
    if not nums or len(nums) < 0:
        return None
    recode = [-float("inf")] * len(nums)
    start = 1
    end = k
    recode[0] = sum(nums[:k])
    while end < len(nums):
        recode[start] = recode[start-1] + nums[end] - nums[start-1]
        start += 1
        end += 1
    return max(recode) / k

if __name__ == '__main__':
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    print(findMaxAverage(nums, k))
