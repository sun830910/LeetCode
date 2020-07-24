# -*- coding: utf-8 -*-

"""
Created on 2020-06-22 23:34
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def missingNumber(nums):
    for idx in range(len(nums)+1):
        if idx not in nums:
            return idx

def missingNumber2(nums):
    target_sum = 0
    for idx in range(len(nums)+1):
        target_sum += idx
    return target_sum - sum(nums)

if __name__ == '__main__':
    print(missingNumber([3, 0, 1]))
    print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
    print(missingNumber([0]))

    print('==========================')
    print(missingNumber2([3, 0, 1]))
    print(missingNumber2([9, 6, 4, 2, 3, 5, 7, 0, 1]))
    print(missingNumber2([0]))