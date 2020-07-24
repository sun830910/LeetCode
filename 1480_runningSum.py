# -*- coding: utf-8 -*-

"""
Created on 2020-06-24 17:50
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def runningSum(nums):
    tmp = nums
    for idx in range(1, len(nums)):
        nums[idx] = nums[idx-1] + tmp[idx]
    return nums

if __name__ == '__main__':
    test1 = [1, 2, 3, 4]
    test2 = [1, 1, 1, 1, 1]
    test3 = [3, 1, 2, 10, 1]

    print(runningSum(test1))
    print(runningSum(test2))
    print(runningSum(test3))