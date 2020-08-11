# -*- coding: utf-8 -*-

"""
Created on 2020-08-11 20:20
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def arrayPairSum(nums):
    nums.sort()
    result = 0
    for idx in range(0, len(nums), 2):
        result += nums[idx]
    return result


if __name__ == '__main__':
    test1 = [1, 4, 3, 2]
    print(arrayPairSum(test1))