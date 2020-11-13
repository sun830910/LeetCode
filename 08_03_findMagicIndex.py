# -*- coding: utf-8 -*-

"""
Created on 2020-11-13 14:41
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def findMagicIndex(nums):
    if not nums or len(nums) == 0:
        return -1
    for idx, value in enumerate(nums):
        if idx == value:
            return idx
    return -1


if __name__ == '__main__':
    nums = [0, 2, 3, 4, 5]
    print(findMagicIndex(nums))
    nums = [1,1,1]
    print(findMagicIndex(nums))
