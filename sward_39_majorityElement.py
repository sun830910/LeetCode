# -*- coding: utf-8 -*-

"""
Created on 1/19/21 10:41 AM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def majorityElement(nums):
    if not nums:
        return
    record = dict()
    target = len(nums) // 2
    for num in nums:
        if num not in record:
            record.setdefault(num, 1)
        else:
            record[num] += 1
        if record[num] > target:
            return num
    return


if __name__ == '__main__':
    nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    print(majorityElement(nums))
