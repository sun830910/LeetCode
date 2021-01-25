# -*- coding: utf-8 -*-

"""
Created on 1/25/21 11:04 AM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def createTargetArray(nums, index):
    target = []
    if not nums or not index:
        return target
    for idx in range(len(nums)):
        target.insert(index[idx], nums[idx])
    return target


if __name__ == '__main__':
    nums = [0, 1, 2, 3, 4]
    index = [0, 1, 2, 2, 1]
    print(createTargetArray(nums, index))
    nums = [1, 2, 3, 4, 0]
    index = [0, 1, 2, 3, 0]
    print(createTargetArray(nums, index))
