# -*- coding: utf-8 -*-

"""
Created on 2020-11-02 19:04
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def searchInsert(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        current = nums[mid]
        if current > target:
            right = mid - 1
        elif current < target:
            left = mid + 1
        else:
            return mid
    if current > target:
        return mid
    else:
        return mid + 1

if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 5
    print(searchInsert(nums, target))  # 2

    nums = [1,3,5,6]
    target = 2
    print(searchInsert(nums, target))  # 1

    nums = [1, 3, 5, 6]
    target = 7
    print(searchInsert(nums, target))  # 4

    nums = [1, 3, 5, 6]
    target = 0
    print(searchInsert(nums, target))  # 0

