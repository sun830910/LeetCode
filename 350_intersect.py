# -*- coding: utf-8 -*-

"""
Created on 2020-09-21 22:17
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def intersect(nums1, nums2):
    result = []
    for idx1 in nums1:
        if idx1 in nums2:
            result.append(idx1)
            nums2.remove(idx1)
    return result

if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(intersect(nums1, nums2))

    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(intersect(nums1, nums2))