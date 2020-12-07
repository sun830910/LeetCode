# -*- coding: utf-8 -*-

"""
Created on 12/7/20 1:57 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def specialArray(nums):
    nums.sort()
    check_idx = -1
    length = len(nums)
    for idx in range(length):
        if length - idx > check_idx and nums[idx] >= length - idx:
            return length - idx
        check_idx = nums[idx]
    return -1


if __name__ == '__main__':
    nums = [0, 4, 3, 0, 4]
    print(specialArray(nums))
