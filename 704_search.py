# -*- coding: utf-8 -*-

"""
Created on 1/29/21 4:28 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def search(nums, target):
    if not nums:
        return -1
    left_idx = 0
    right_idx = len(nums)
    while left_idx < right_idx:
        mid_idx = (left_idx + right_idx) // 2
        num = nums[mid_idx]
        if num == target:
            return mid_idx
        elif num > target:
            right_idx = mid_idx
        else:
            left_idx = mid_idx + 1
    return -1


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(search(nums, target))
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    print(search(nums, target))
