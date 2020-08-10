# -*- coding: utf-8 -*-

"""
Created on 2020-08-10 23:23
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def rotate(nums, k):
    length = len(nums)
    nums[:] = nums[length-k:] + nums[:length-k]
    print(nums)

if __name__ == '__main__':
    test1 =[1, 2, 3, 4, 5, 6, 7]
    k1 = 3
    rotate(test1, k1)

    test2 = [-1, -100, 3, 99]
    k2 = 2
    rotate(test2, k2)