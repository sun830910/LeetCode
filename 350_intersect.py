# -*- coding: utf-8 -*-

"""
Created on 11/26/20 9:40 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def intersect(nums1, nums2):
    result = []
    record1 = dict()
    record2 = dict()
    for num in nums1:
        if num not in record1:
            record1.setdefault(num, 1)
        else:
            record1[num] += 1
    for num in nums2:
        if num not in record2:
            record2.setdefault(num, 1)
        else:
            record2[num] += 1
    for key in record1:
        if key in record2:
            result += [key] * min(record1.get(key), record2.get(key))
    return result


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(intersect(nums1, nums2))
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(intersect(nums1, nums2))
