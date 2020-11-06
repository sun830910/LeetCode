# -*- coding: utf-8 -*-

"""
Created on 2020-11-07 00:01
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


# 效率过低
# def missingNumber(nums):
#     for idx in range(len(nums)+1):
#         if idx not in nums:
#             return idx
#     return None

def missingNumber(nums):
    nums_set = set(nums)
    for idx in range(len(nums)+1):
        if idx not in nums_set:
            return idx
    return None


if __name__ == '__main__':
    nums = [3, 0, 1]
    print(missingNumber(nums))

    nums = [0, 1]
    print(missingNumber(nums))

    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(missingNumber(nums))
