# -*- coding: utf-8 -*-

"""
Created on 2020-11-09 09:47
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def bubbleSort(nums):
    for idx1 in range(len(nums) - 1):
        for idx2 in range(len(nums) - idx1 - 1):
            if nums[idx2] > nums[idx2 + 1]:
                nums[idx2], nums[idx2 + 1] = nums[idx2 + 1], nums[idx2]
    return nums


if __name__ == '__main__':
    nums = [1, 5, 3, 7, 9, 2, 7, 4]
    print(bubbleSort(nums))
