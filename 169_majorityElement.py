# -*- coding: utf-8 -*-

"""
Created on 2020-11-03 20:57
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""
# 时间复杂度 O(N)
# def majorityElement(nums):
#     n = len(nums)
#     if n == 1:
#         return nums[0]
#     note = dict()
#     for num in nums:
#         if num not in note:
#             note.setdefault(num, 1)
#         else:
#             note[num] += 1
#             if note[num] > (n/2):
#                 return num
#     return None

def majorityElement(nums):
    count = 0
    candidate = nums[0]
    for num in nums:
        if count == 0:
            candidate = num
        if candidate == num:
            count += 1
        else:
            count -= 1


    return candidate

if __name__ == '__main__':
    nums = [3, 2, 3]
    print(majorityElement(nums))

    nums = [1]
    print(majorityElement(nums))

    nums = [2, 2, 1, 1, 1, 2, 2]
    print(majorityElement(nums))
