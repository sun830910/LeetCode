# -*- coding: utf-8 -*-

"""
Created on 2020-07-15 23:27
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def insertSort(nums):
    for idx in range(len(nums)):
        done_idx = idx-1
        current = nums[idx]
        while current < nums[done_idx] and done_idx >= 0:
            nums[done_idx+1] =nums[done_idx]
            done_idx -= 1
        nums[done_idx+1] = current
    return nums

test = [1,5,2,3,8,6,7,4,9]
print(insertSort(test))