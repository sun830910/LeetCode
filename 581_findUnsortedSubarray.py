# -*- coding: utf-8 -*-

"""
Created on 2020-08-18 23:13
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def findUnsortedSubarray(nums):
    left = 0
    right = 0
    for idx in range(len(nums)-1):
        if nums[idx] > nums[idx+1]:
            left = idx  # 1
            break
    for idx in range(len(nums)-1, 0, -1):
        if nums[idx] < nums[idx-1]:
            right = idx  # 5
            break
    if left == right == 0:
        return 0

    min_num = min(nums[left:right+1])  # 4
    max_num = max(nums[left:right+1])  # 10

    for idx in range(len(nums[0:left])):
        if nums[idx] > min_num:
            left = idx
            break
    for idx in range(len(nums)-1, right, -1):
        if nums[idx] < max_num:
            right = idx
            break
    return right-left+1


if __name__ == '__main__':
    test = [2, 6, 4, 8, 10, 9, 15]  # 5
    print(findUnsortedSubarray(test))
