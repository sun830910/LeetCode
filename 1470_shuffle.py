# -*- coding: utf-8 -*-

"""
Created on 2020-06-24 16:11
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def shuffle(nums, n):
    if not nums or not n:
        return
    left = nums[:n]
    right = nums[n:]
    result = []
    for idx in range(n):
        result.append(left[idx])
        result.append(right[idx])
    return result

if __name__ == '__main__':
    print(shuffle(nums = [2,5,1,3,4,7], n = 3))
    print(shuffle(nums = [1,2,3,4,4,3,2,1], n = 4))
    print(shuffle(nums = [1,1,2,2], n = 2))