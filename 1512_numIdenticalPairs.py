# -*- coding: utf-8 -*-

"""
Created on 1/21/21 8:39 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def numIdenticalPairs(nums):
    result = 0
    if not nums:
        return result
    record = dict()
    for idx in range(len(nums)):
        if nums[idx] not in record:
            record.setdefault(nums[idx], [idx])
        else:
            record[nums[idx]].append(idx)
    for val in record.values():
        result += ((len(val) * (len(val) - 1)) // 2)
    return result


if __name__ == '__main__':
    nums = [1, 2, 3, 1, 1, 3]
    print(numIdenticalPairs(nums))
    nums = [1, 1, 1, 1]
    print(numIdenticalPairs(nums))
    nums = [1, 2, 3]
    print(numIdenticalPairs(nums))
