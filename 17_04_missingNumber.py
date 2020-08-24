# -*- coding: utf-8 -*-

"""
Created on 2020-08-24 18:21
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def missingNumber(nums):
    length = len(nums)
    return ((length+1 + 0) * length // 2) - sum(nums)

if __name__ == '__main__':
    test1 = [1, 0, 3]
    print(missingNumber(test1))