# -*- coding: utf-8 -*-

"""
Created on 1/24/21 4:04 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def smallerNumbersThanCurrent(nums):
    arr = [0] * 101
    result = []
    for num in nums:
        arr[num] += 1
    for idx in range(1, len(arr)):
        arr[idx] += arr[idx - 1]
    for num in nums:
        if num == 0:
            result.append(0)
        else:
            result.append(arr[num - 1])
    return result


if __name__ == '__main__':
    # nums = [8, 1, 2, 2, 3]
    # print(smallerNumbersThanCurrent(nums))
    # nums = [6, 5, 4, 8]
    # print(smallerNumbersThanCurrent(nums))
    # nums = [7, 7, 7, 7]
    # print(smallerNumbersThanCurrent(nums))
    nums = [5, 0, 10, 0, 10, 6]
    print(smallerNumbersThanCurrent(nums))
