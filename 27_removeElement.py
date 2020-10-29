# -*- coding: utf-8 -*-

"""
Created on 2020-10-29 20:56
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def removeElement(nums, val):
    if (nums is None) or (len(nums) == 0):
        return 0
    checked = 0
    for idx in range(len(nums)):
        if nums[idx] != val:
            nums[checked], nums[idx] = nums[idx], nums[checked]
            checked += 1
    return checked


if __name__ == '__main__':
    sample = [3, 2, 2, 3]
    target = 3
    print(removeElement(sample, target))
    print(sample)

    sample = [0, 1, 2, 2, 3, 0, 4, 2]
    target = 2
    print(removeElement(sample, target))
    print(sample)
