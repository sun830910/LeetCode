# -*- coding: utf-8 -*-

"""
Created on 2020-09-18 17:22
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    result = []
    for idx1 in set1:
        if idx1 in set2 and idx1 not in result:
            result.append(idx1)
    return result

if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(intersection(nums1, nums2))

    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(intersection(nums1, nums2))

