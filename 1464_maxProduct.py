# -*- coding: utf-8 -*-

"""
Created on 11/30/20 5:35 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def maxProduct(nums):
    first_min = float("inf")
    second_min = float("inf")
    first_max = - float("inf")
    second_max = - float("inf")
    for idx, num in enumerate(nums):
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num > second_max:
            second_max = num
        if num < first_min:
            second_min = first_min
            first_min = num
        elif num < second_min:
            second_min = num
    return max((first_max - 1) * (second_max - 1), (first_min - 1) * (second_min - 1))


if __name__ == '__main__':
    nums = [3, 4, 5, 2]
    print(maxProduct(nums))
    nums = [1, 5, 4, 5]
    print(maxProduct(nums))
    nums = [3, 7]
    print(maxProduct(nums))
    nums = [1]
    print(maxProduct(nums))