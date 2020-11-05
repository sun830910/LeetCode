# -*- coding: utf-8 -*-

"""
Created on 2020-11-05 23:44
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def moveZeroes(nums):
    first = True
    for idx, num in enumerate(nums):
        if num != 0 and first == False:
            nums[idx], nums[zero_idx] = nums[zero_idx], nums[idx]
            zero_idx += 1
        if num == 0 and first == True:
            first = False
            zero_idx = idx
    return nums


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    print(moveZeroes(nums))
    nums = [1, 3, 5, 0, 9]
    print(moveZeroes(nums))
