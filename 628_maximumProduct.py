# -*- coding: utf-8 -*-

"""
Created on 2020-11-06 23:27
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def maximumProduct(nums):
    max_first, max_second, max_third = -float("inf"), -float("inf"), -float("inf")
    min_first, min_second = float("inf"), float("inf")

    for num in nums:
        if num > max_first:
            max_third = max_second
            max_second = max_first
            max_first = num
        elif num > max_second:
            max_third = max_second
            max_second = num
        elif num > max_third:
            max_third = num

        if num < min_first:
            min_second = min_first
            min_first = num
        elif num < min_second:
            min_second = num
    return max(max_first * max_second * max_third, min_first * min_second * max_first)


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(maximumProduct(nums))
    nums = [1, 2, 3, 4]
    print(maximumProduct(nums))