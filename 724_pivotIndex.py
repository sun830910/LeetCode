# -*- coding: utf-8 -*-

"""
Created on 2020-11-18 09:50
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


#  约 20 %
# def pivotIndex(nums):
#     for idx, value in enumerate(nums):
#         if sum(nums[:idx]) == sum(nums[idx + 1:]):
#             return idx
#     return -1

#  35 %
# def pivotIndex(nums):
#     n = len(nums)
#     if n == 0:
#         return -1
#     left, right = {0: 0}, {n - 1: 0}
#     for idx in range(1, len(nums)):
#         left[idx] = left[idx - 1] + nums[idx - 1]
#     for idx in range(len(nums) - 2, -1, -1):
#         right[idx] = right[idx + 1] + nums[idx + 1]
#     for key in left:
#         if left[key] == right[key]:
#             return key
#     return -1

def pivotIndex(nums):
    if not nums:
        return -1
    current = 0
    total = sum(nums)
    for idx in range(len(nums)):
        if current * 2 + nums[idx] == total:
            return idx
        current += nums[idx]
    return -1


if __name__ == '__main__':
    nums = [1, 7, 3, 6, 5, 6]
    print(pivotIndex(nums))

    nums = [1, 2, 3]
    print(pivotIndex(nums))
