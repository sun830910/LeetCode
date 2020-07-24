# -*- coding: utf-8 -*-

"""
Created on 2020-07-15 23:15
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def bubbleSort(nums):
    for idx1 in range(1, len(nums)):
        for idx2 in range(len(nums)-idx1):
            if nums[idx2] > nums[idx2+1]:
                nums[idx2], nums[idx2+1] = nums[idx2+1], nums[idx2]
    return nums

test = [1,5,2,3,8,6,7,4,9]
print(bubbleSort(test))