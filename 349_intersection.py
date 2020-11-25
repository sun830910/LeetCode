# -*- coding: utf-8 -*-

"""
Created on 11/25/20 6:22 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def intersection(nums1, nums2):
    set_1 = set(nums1)
    set_2 = set(nums2)
    result = []
    length1 = len(set_1)
    length2 = len(set_2)
    if length1 < length2:
        for val in set_1:
            if val in set_2:
                result.append(val)
    else:
        for val in set_2:
            if val in set_1:
                result.append(val)
    return result


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(intersection(nums1, nums2))

    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(intersection(nums1, nums2))
