# -*- coding: utf-8 -*-

"""
Created on 12/7/20 4:58 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def runningSum(nums):
    if not nums:
        return
    result = [0] * len(nums)
    result[0] = nums[0]
    for idx in range(1, len(nums)):
        result[idx] = result[idx - 1] + nums[idx]
    return result


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(runningSum(nums))
    nums = [1, 1, 1, 1, 1]
    print(runningSum(nums))
    nums = [3, 1, 2, 10, 1]
    print(runningSum(nums))
