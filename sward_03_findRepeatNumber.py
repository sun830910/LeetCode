# -*- coding: utf-8 -*-

"""
Created on 2020-11-11 16:28
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


# 速度较快，约90%
def findRepeatNumber(nums):
    record = set()
    for num in nums:
        if num in record:
            return num
        else:
            record.add(num)
    return -1


# 速度较慢，低于10%
# def findRepeatNumber(nums):
#     record = set()
#     for idx in range(len(nums)):
#         record.add(idx)
#     for num in nums:
#         if num not in record:
#             return num
#         record.remove(num)
#     return -1


if __name__ == '__main__':
    nums = [2, 3, 1, 0, 2, 5, 3]
    print(findRepeatNumber(nums))
    nums = [0, 1, 2, 3, 4, 11, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print(findRepeatNumber(nums))
