# -*- coding: utf-8 -*-

"""
Created on 2020-11-06 17:39
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def findMaxAverage(nums, k):
    if not nums or len(nums) < 0:
        return None
    recode = [0] * (len(nums) - k + 1)
    for idx in range(len(recode)):
        recode[idx] = sum(nums[idx:idx + k])
    return max(recode) / k

if __name__ == '__main__':
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    print(findMaxAverage(nums, k))