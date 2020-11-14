# -*- coding: utf-8 -*-

"""
Created on 2020-11-14 18:26
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def dominantIndex(nums):
    if not nums:
        return -1
    max_num = max(set(nums))
    result = 0
    for idx, num in enumerate(nums):
        if num != max_num and num * 2 > max_num:
            return -1
        elif num == max_num:
            result = idx
    return result


if __name__ == '__main__':
    nums = [3, 6, 1, 0]
    print(dominantIndex(nums))
    nums = [1, 2, 3, 4]
    print(dominantIndex(nums))