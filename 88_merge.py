# -*- coding: utf-8 -*-

"""
Created on 2020-11-02 20:25
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def merge(nums1, m, nums2, n):
    idx1 = m - 1
    idx2 = n - 1
    current = m + n - 1
    while current >= 0 and idx1 >= 0 and idx2 >= 0:
        if nums1[idx1] >= nums2[idx2]:
            nums1[current] = nums1[idx1]
            idx1 -= 1
        else:
            nums1[current] = nums2[idx2]
            idx2 -= 1
        current -= 1
    if idx2 >= 0:
        nums1[:current+1] = nums2[:idx2+1]
        
    return nums1




if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(merge(nums1, m, nums2, n))

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [0, 0, 0]
    n = 3
    print(merge(nums1, m, nums2, n))

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [4, 5, 6]
    n = 3
    print(merge(nums1, m, nums2, n))

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3
    print(merge(nums1, m, nums2, n))

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    print(merge(nums1, m, nums2, n))