# -*- coding: utf-8 -*-

"""
Created on 2020-08-27 23:48
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def findMagicIndex(nums):
    idx = 0
    while idx < len(nums):
        if nums[idx] > idx:
            idx = nums[idx]
        elif nums[idx] == idx:
            return idx
        else:
            idx += 1
    return -1


if __name__ == '__main__':
    nums = [0, 2, 3, 4, 5]  # 0
    print(findMagicIndex(nums))

    nums = [1, 1, 1]  # 1
    print(findMagicIndex(nums))

    nums = [0]
    print(findMagicIndex(nums))
