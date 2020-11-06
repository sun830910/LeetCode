# -*- coding: utf-8 -*-

"""
Created on 2020-11-06 23:53
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def findDisappearedNumbers(nums):
    support = set(nums)
    result = [idx + 1 for idx in range(len(nums))]
    for num in support:
        if num in result:
            result.remove(num)
    return result


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(findDisappearedNumbers(nums))
    nums = [1, 1]
    print(findDisappearedNumbers(nums))
