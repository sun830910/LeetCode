# -*- coding: utf-8 -*-

"""
Created on 2020-08-11 20:26
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def maximumProduct(nums):
    nums.sort()

    return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])

if __name__ == '__main__':

    test1 = [1,2,3]
    print(maximumProduct(test1))

    test2 = [1,2,3,4]
    print(maximumProduct(test2))