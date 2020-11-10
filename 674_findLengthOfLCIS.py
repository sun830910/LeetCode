# -*- coding: utf-8 -*-

"""
Created on 2020-11-10 16:41
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def findLengthOfLCIS(nums):
    if not nums or len(nums) == 0:
        return 0

    max_cnt = 0
    cnt = 0
    for idx in range(len(nums) - 1):
        if nums[idx] < nums[idx + 1]:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 0
    max_cnt = max(max_cnt, cnt)
    return max_cnt + 1


if __name__ == '__main__':
    nums = [1, 3, 4, 7, 8, 9]
    print(findLengthOfLCIS(nums))
    nums = []
    print(findLengthOfLCIS(nums))