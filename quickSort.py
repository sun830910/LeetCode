# -*- coding: utf-8 -*-

"""
Created on 2020-07-24 19:35
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

import random

def swap(nums, idx1, idx2):
    nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
    return nums

def partition(nums, L, R):
    less = L - 1
    more = R
    while L < more:
        if nums[L] < nums[R]:
            less += 1
            swap(nums, less, L)
            L += 1
        elif nums[L] > nums[R]:
            more -= 1
            swap(nums, more, L)
        else:
            L += 1
    swap(nums, more, R)
    return [less+1, more]

def quickSort(nums, L, R):
    if L < R:
        swap(nums, L + int(random.random() * (R - L+1)), R)
        result = partition(nums, L, R)
        quickSort(nums, L, result[0]-1)
        quickSort(nums, result[1]+1, R)



if __name__ == '__main__':

    test1 = [2, 1, 4, 3]
    quickSort(test1, 0, len(test1)-1)
    print(test1)
