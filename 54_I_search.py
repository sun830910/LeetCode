# -*- coding: utf-8 -*-

"""
Created on 2020-08-30 23:33
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def search(nums, target):
    cnt = 0
    for num in nums:
        if num == target:
            cnt += 1
        if num > target:
            return cnt
    return cnt

if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(search(nums, target))

    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    print(search(nums, target))
