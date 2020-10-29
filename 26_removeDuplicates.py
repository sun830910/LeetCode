# -*- coding: utf-8 -*-

"""
Created on 2020-10-29 20:21
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def removeDuplicates(nums):
    if (nums is None) or (len(nums) == 0):
        return 0

    checked = 0
    for idx in range(1, len(nums)):
        if nums[checked] != nums[idx]:
            checked += 1
            nums[checked] = nums[idx]
    return checked + 1


if __name__ == '__main__':
    sample = [1, 1, 2, 2]
    print(removeDuplicates(sample))  # 2
    print(sample)

    sample = [0,0,1,1,1,2,2,3,3,4]
    print(removeDuplicates(sample))  # 5
    print(sample)

