# -*- coding: utf-8 -*-

"""
Created on 1/19/21 11:04 AM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def exchange(nums):
    left_idx, right_idx = 0, len(nums) - 1
    while left_idx <= right_idx:
        left_num = nums[left_idx]
        right_num = nums[right_idx]
        if left_num % 2 == 1:
            left_idx += 1
        if right_num % 2 == 0:
            right_idx -= 1
        if left_num % 2 == 0 and right_num % 2 == 1:
            nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]
    return nums


def exchange2(nums):
    left_idx, right_idx = 0, len(nums) - 1
    while left_idx <= right_idx:
        left_flag = True if nums[left_idx] % 2 == 1 else False
        right_flag = True if nums[right_idx] % 2 == 0 else False
        if left_flag:
            left_idx += 1
        if right_flag:
            right_idx -= 1
        if not left_flag and not right_flag:
            nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]

    return nums


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(exchange(nums))
    nums = [1, 2, 3, 4]
    print(exchange2(nums))
