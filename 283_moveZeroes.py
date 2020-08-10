# -*- coding: utf-8 -*-

"""
Created on 2020-08-10 22:47
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def moveZeroes(nums):
    zero_cnt = 0
    for num in nums:
        if num == 0:
            zero_cnt += 1

    for _ in range(zero_cnt):
        nums.remove(0)
        nums.append(0)

    return nums

if __name__ == '__main__':
    test1 = [0,1,0,3,12]
    print(moveZeroes(test1))