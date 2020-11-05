# -*- coding: utf-8 -*-

"""
Created on 2020-11-05 23:27
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def thirdMax(nums):
    if len(set(nums)) < 3:
        return max(nums)
    first, second, third = -float('inf'), -float('inf'), -float('inf')
    for num in nums:
        if num != first and num != second and num != third:
            if num > first:
                third = second
                second = first
                first = num
            elif num > second:
                third = second
                second = num
            elif num > third:
                third = num
    return third


if __name__ == '__main__':
    nums = [3, 2, 1]
    print(thirdMax(nums))
    nums = [1, 2]
    print(thirdMax(nums))
    nums = [2, 2, 3, 1]
    print(thirdMax(nums))
    nums = [1, 2, 2]
    print(thirdMax(nums))
    nums = [0, 1, 2]
    print(thirdMax(nums))
