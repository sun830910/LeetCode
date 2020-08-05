# -*- coding: utf-8 -*-

"""
Created on 2020-08-05 23:21
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def relativeSortArray(arr1, arr2):
    nums = dict()
    for arr1_idx in arr1:
        if arr1_idx not in nums:
            nums.setdefault(arr1_idx, 1)
        else:
            nums[arr1_idx] += 1
    result = []
    for arr2_idx in arr2:
        if arr2_idx in nums:
            cnt = nums[arr2_idx]
            for _ in range(cnt):
                result.append(arr2_idx)
            del nums[arr2_idx]
    if len(nums) > 0:
        tmp = sorted(nums.keys())
        print(sorted(tmp))
        for tmp_idx in tmp:
            cnt = nums[tmp_idx]
            for _ in range(cnt):
                result.append(tmp_idx)
        del nums[tmp_idx]
    return result

if __name__ == '__main__':
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    print(relativeSortArray(arr1, arr2))