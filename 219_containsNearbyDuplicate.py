# -*- coding: utf-8 -*-

"""
Created on 2020-11-05 23:19
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def containsNearbyDuplicate(nums, k):
    record = dict()
    for idx, num in enumerate(nums):
        if num not in record:
            record.setdefault(num, idx)
        else:
            if idx - record.get(num) <= k:
                return True
            else:
                record[num] = idx
    return False


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    k = 3
    print(containsNearbyDuplicate(nums, k))

    nums = [1, 0, 1, 1]
    k = 1
    print(containsNearbyDuplicate(nums, k))

    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    print(containsNearbyDuplicate(nums, k))
