# -*- coding: utf-8 -*-

"""
Created on 2020-05-31 22:10
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def merge(nums1, m, nums2, n):
    idx1, idx2 = 0, 0
    while idx2 < n:
        if idx1 >= m + idx2:
            nums1[idx1:idx1+n-idx2] = nums2[idx2:n]
            break
        if nums1[idx1] < nums2[idx2]:
            idx1 += 1
        else:
            nums1[idx1+1:] = nums1[idx1:len(nums1)-1]
            nums1[idx1] = nums2[idx2]
            idx1 += 1
            idx2 += 1

    return nums1
if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(merge(nums1, m ,nums2, n))

    nums3 = [2, 5, 6, 0, 0, 0]
    nums4 = [1, 2, 3]
    print(merge(nums3, m, nums4, n))
