# -*- coding: utf-8 -*-

"""
Created on 2020-11-11 14:21
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def majorityElement(nums):
    if not nums or len(nums) == 0:
        return
    record = dict()
    for num in nums:
        if num not in record:
            record.setdefault(num, 1)
        else:
            record[num] += 1
        if record[num] > len(nums) // 2:
            return num
    return -1


if __name__ == '__main__':
    nums = [1, 2, 5, 9, 5, 9, 5, 5, 5]
    print(majorityElement(nums))
    nums = [3, 2]
    print(majorityElement(nums))
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(majorityElement(nums))
    nums = [1]
    print(majorityElement(nums))

