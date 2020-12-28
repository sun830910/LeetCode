# -*- coding: utf-8 -*-

"""
Created on 12/28/20 7:47 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def rob(nums):
    length = len(nums)
    if length == 0:
        return 0
    elif length == 1:
        return nums[0]
    elif length == 2:
        return max(nums)
    elif length == 3:
        return max(nums[0] + nums[2], nums[1])

    result = [0] * length
    result[0] = nums[0]
    result[1] = nums[1]
    result[2] = nums[0] + nums[2]
    for idx in range(3, length):
        result[idx] = max(result[idx - 2] + nums[idx], result[idx - 3] + nums[idx])
    return max(result[-2:])


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(rob(nums))
    nums = [2, 7, 9, 3, 1]
    print(rob(nums))
