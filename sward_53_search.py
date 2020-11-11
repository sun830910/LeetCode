# -*- coding: utf-8 -*-

"""
Created on 2020-11-11 16:42
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


# 双指针，92%
def search(nums, target):
    left_idx = 0
    right_idx = len(nums) - 1
    if target not in set(nums):
        return 0
    while (nums[left_idx] != target or nums[right_idx] != target) and left_idx <= right_idx:
        if nums[left_idx] != target and left_idx <= right_idx:
            left_idx += 1
        if nums[right_idx] != target and left_idx <= right_idx:
            right_idx -= 1
    return right_idx - left_idx + 1


"""
没看清楚题目是排序数组，底下的做法可以用在非排序数组。
"""
# def search(nums, target):  # 8%
#     cnt = 0
#     while target in set(nums):
#         cnt += 1
#         nums.remove(target)
#     return cnt


# def search(nums, target):  # 8%
#     if target not in set(nums):
#         return 0
#     cnt = 0
#     while target in nums:
#         cnt += 1
#         nums.remove(target)
#     return cnt


# def search(nums, target):  # 16.16%
#     if target not in set(nums):
#         return 0
#     cnt = 0
#     for num in nums:
#         if num == target:
#             cnt += 1
#     return cnt


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(search(nums, target))
    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    print(search(nums, target))
