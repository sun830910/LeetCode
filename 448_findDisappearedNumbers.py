# -*- coding: utf-8 -*-

"""
Created on 2020-11-06 23:53
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def findDisappearedNumbers(nums):
    support = set(nums)
    result = []
    for idx in range(1, len(nums)+1):
        if idx not in support:
            result.append(idx)
    return result


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(findDisappearedNumbers(nums))
    nums = [1, 1]
    print(findDisappearedNumbers(nums))
