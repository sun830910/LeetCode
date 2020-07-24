# -*- coding: utf-8 -*-

"""
Created on 2020-07-16 00:20
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def duplicateZeros(nums):
    idx = 0
    while idx < len(nums):
        if nums[idx] == 0:
            nums.pop()
            nums.insert(idx+1, 0)
            idx +=1
        idx += 1
    print(nums)
duplicateZeros([1,0,2,3,0,4,5,0])