# -*- coding: utf-8 -*-

"""
Created on 2020-11-09 09:54
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def selectSort(nums):
    for idx1 in range(len(nums)):
        min_idx = idx1
        for idx2 in range(idx1, len(nums)):
            if nums[idx2] < nums[min_idx]:
                min_idx = idx2
        nums[min_idx], nums[idx1] = nums[idx1], nums[min_idx]
    return nums


if __name__ == '__main__':
    nums = [64, 25, 12, 22, 11]
    print(selectSort(nums))
