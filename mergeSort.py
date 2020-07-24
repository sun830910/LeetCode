# -*- coding: utf-8 -*-

"""
Created on 2020-07-15 23:35
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def mergeSort(nums):
    if len(nums) < 2:
        return nums

    mid_idx = len(nums)//2
    left, right = nums[:mid_idx], nums[mid_idx:]
    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

test = [1,5,2,3,8,6,7,4,9]
print(mergeSort(test))
