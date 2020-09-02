# -*- coding: utf-8 -*-

"""
Created on 2020-09-02 23:31
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def findRepeatNumber(nums):
    num_cnt = dict()
    for num in nums:
        if num not in num_cnt:
            num_cnt.setdefault(num, 1)
        else:
            return num


if __name__ == '__main__':
    test1 =[2, 3, 1, 0, 2, 5, 3]
    print(findRepeatNumber(test1))