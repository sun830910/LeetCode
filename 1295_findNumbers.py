# -*- coding: utf-8 -*-

"""
Created on 12/1/20 5:39 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def findNumbers(nums):
    cnt = 0
    if not nums:
        return cnt
    for num in nums:
        length = len(str(num))
        if length % 2 == 0:
            cnt += 1
    return cnt

if __name__ == '__main__':
    nums = [12, 345, 2, 6, 7896]
    print(findNumbers(nums))