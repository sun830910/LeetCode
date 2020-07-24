# -*- coding: utf-8 -*-

"""
Created on 2020-07-15 23:22
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def selectSort(nums):
    for idx1 in range(len(nums)):
        min_idx = idx1
        for idx2 in range(idx1+1, len(nums)):
            if nums[idx2] < nums[min_idx]:
                min_idx = idx2
        nums[idx1], nums[min_idx] = nums[min_idx], nums[idx1]
    return nums

test = [1,5,2,3,8,6,7,4,9]

print(selectSort(test))

