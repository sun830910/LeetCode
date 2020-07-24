# -*- coding: utf-8 -*-

"""
Created on 2020-05-28 00:27
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def removeDuplicates(nums):
    if not nums:
        return 0

    length=len(nums)
    # 负责计算不重复的部分指针
    new_idx = 0
    # 负责遍历整个数组
    check_idx = 1
    while check_idx < length:
        if nums[new_idx] != nums[check_idx]:
            new_idx += 1
            nums[new_idx] = nums[check_idx]
        else:
            check_idx+=1
    return new_idx+1

if __name__ == '__main__':
    nums = [1, 1, 2]
    print(removeDuplicates(nums))
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(removeDuplicates(nums2))
    nums3 = [1]
    print(removeDuplicates(nums3))