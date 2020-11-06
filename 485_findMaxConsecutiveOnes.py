# -*- coding: utf-8 -*-

"""
Created on 2020-11-06 17:29
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def findMaxConsecutiveOnes(nums):
    max_length = 0
    current_length = 0
    for num in nums:
        if num == 1:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 0
        max_length = max(max_length, current_length)
    return max_length


if __name__ == '__main__':
    nums = [1, 1, 0, 1, 1, 1]
    print(findMaxConsecutiveOnes(nums))
