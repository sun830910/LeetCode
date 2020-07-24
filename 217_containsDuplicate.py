# -*- coding: utf-8 -*-

"""
Created on 2020-06-22 23:17
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def containsDuplicate(nums):
    if nums is None:
        return
    return len(nums) != len(set(nums))

if __name__ == '__main__':
    test1 = [1,2,3,1]
    test2 = [1,2,3,4]
    test3 = [1,1,1,3,3,4,3,2,4,2]
    print(containsDuplicate(test1))
    print(containsDuplicate(test2))
    print(containsDuplicate(test3))