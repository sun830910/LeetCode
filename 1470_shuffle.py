# -*- coding: utf-8 -*-

"""
Created on 12/2/20 9:49 AM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def shuffle(nums, n):
    if not nums:
        return
    result = []
    left = nums[:n]
    right = nums[n:]
    assert len(left) == len(right)
    idx = 0
    while idx < n:
        result.append(left[idx])
        result.append(right[idx])
        idx += 1
    return result


if __name__ == '__main__':
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    print(shuffle(nums, n))  # [2,3,5,4,1,7]

    nums = [1, 2, 3, 4, 4, 3, 2, 1]
    n = 4
    print(shuffle(nums, n))

    nums = [1, 1, 2, 2]
    n = 2
    print(shuffle(nums, n))  # [1, 2, 1, 2]

