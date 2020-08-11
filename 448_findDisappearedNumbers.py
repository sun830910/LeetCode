# -*- coding: utf-8 -*-

"""
Created on 2020-08-10 23:46
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def findDisappearedNumbers(nums):
    nums_set = set(nums)
    result = []
    for idx in range(1, len(nums)+1):
        if idx not in nums_set:
            result.append(idx)
    return result

if __name__ == '__main__':
    test1 = [4,3,2,7,8,2,3,1]
    print(findDisappearedNumbers(test1))
    test2 = [1,1]
    print(findDisappearedNumbers(test2))