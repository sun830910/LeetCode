# -*- coding: utf-8 -*-

"""
Created on 2020-11-13 15:03
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


# 遍历查找，时间复杂度O(N)
# def missingNumber(nums):
#     record = set(idx for idx in range(len(nums) + 1))
#     for num in nums:
#         if num in record:
#             record.remove(num)
#     return record.pop()

def missingNumber(nums):
    left = 0
    right = len(nums) - 1
    while right >= left:
        mid = (left + right) // 2
        if nums[mid] != mid:
            right = mid - 1
        else:
            left = mid + 1
    return left


if __name__ == '__main__':
    nums = [0, 1, 3]
    print(missingNumber(nums))
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 9]
    print(missingNumber(nums))
    nums = [0, 1, 2]
    print(missingNumber(nums))
    nums = [1, 2, 3]
    print(missingNumber(nums))
