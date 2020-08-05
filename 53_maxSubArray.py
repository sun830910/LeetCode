# -*- coding: utf-8 -*-

"""
Created on 2020-08-05 23:41
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def maxSubArray(nums):
    for idx in range(1, len(nums)):
        nums[idx] = max(nums[idx-1]+nums[idx], nums[idx])
    return max(nums)

if __name__ == '__main__':
    test = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(test))