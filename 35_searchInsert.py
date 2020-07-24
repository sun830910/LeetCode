# -*- coding: utf-8 -*-

"""
Created on 2020-05-28 00:54
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def searchInsert(nums, target):
    if nums[-1] < target:
        return len(nums)

    right_idx = len(nums)-1
    left_idx = 0
    ans = -1
    while left_idx<=right_idx:
        mid = (left_idx+right_idx)//2
        # target应该插入在mid的左边
        if nums[mid]>=target:
            right_idx = mid-1
            ans = mid
        # target应该插在mid的右边
        else:
            left_idx = mid+1
    return ans

if __name__ == '__main__':
    nums1 = [1, 3, 5, 6]
    target1 = 5
    print(searchInsert(nums1,target1))
    nums2 = [1, 3, 5, 6]
    target2 = 0
    print(searchInsert(nums2, target2))