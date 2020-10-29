# -*- coding: utf-8 -*-

"""
Created on 2020-10-29 20:07
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def twoSum(nums, target):
    note = dict()
    for nums_idx in range(len(nums)):
        if target - nums[nums_idx] in note:
            return [note.get(target-nums[nums_idx]), nums_idx]
        else:
            note.setdefault(nums[nums_idx], nums_idx)
    return


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))
