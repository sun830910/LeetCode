# -*- coding: utf-8 -*-

"""
Created on 2020-08-05 23:46
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def majorityElement(nums):
    tmp = dict()
    for num in nums:
        if num not in tmp:
            tmp.setdefault(num, 1)
        else:
            tmp[num] += 1
        if tmp[num] > len(nums) / 2:
            return num
    return -1

if __name__ == '__main__':
    test1 = [1,2,5,9,5,9,5,5,5]
    print(majorityElement(test1))

    test2 = [3,2]
    print(majorityElement(test2))

    test3 = [2,2,1,1,1,2,2]
    print(majorityElement(test3))

    test4 = [1]
    print(majorityElement(test4))