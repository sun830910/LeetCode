# -*- coding: utf-8 -*-

"""
Created on 2020-05-28 00:46
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def removeElement(nums, val):
    check_idx = 0
    done_idx = 0
    while check_idx<len(nums):
        if nums[check_idx] == val:
            check_idx+=1
        else:
            nums[done_idx]=nums[check_idx]
            done_idx+=1
            check_idx+=1
    return done_idx

if __name__ == '__main__':
    nums1 = [3, 2, 2, 3]
    val1 = 3
    print(removeElement(nums1, val1))

    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    print(removeElement(nums2, val2))