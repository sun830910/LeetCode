# -*- coding: utf-8 -*-

"""
Created on 2020-11-05 23:12
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def containsDuplicate(nums):
    if (len(nums)) == len(set(nums)):
        return False
    return True

if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(containsDuplicate(nums))
    nums = [1, 2, 3, 4]
    print(containsDuplicate(nums))
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(containsDuplicate(nums))
