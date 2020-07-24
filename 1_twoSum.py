# -*- coding: utf-8 -*-

"""
Created on 2020-05-25 22:35
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def twoSum(nums, target):
    for idx in range(len(nums)):
        if target - nums[idx] in nums:
            if nums.index(target-nums[idx]) != idx:
                return [idx, nums.index(target-nums[idx])]
    return []

def twoSum2(nums, target):
    HashMap = {}
    for idx, num in enumerate(nums):
        # 若在num中
        if HashMap.get(target-num) is not None:
            return [idx, HashMap.get(target-num)]
        HashMap[num] = idx


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums,target))
    print(twoSum2(nums, target))