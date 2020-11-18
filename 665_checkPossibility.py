# -*- coding: utf-8 -*-

"""
Created on 2020-11-18 09:06
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def checkPossibility(nums):
    cnt = 0
    for idx in range(1, len(nums)):
        if nums[idx] < nums[idx-1]:
            cnt += 1
            if len(nums) - 1 > idx >= 2:
                if nums[idx] < nums[idx-2] and nums[idx+1] < nums[idx-1]:
                    return False
        if cnt > 1:
            return False
    return True


if __name__ == '__main__':
    nums = [4, 2, 3]
    print(checkPossibility(nums))
    nums = [4, 2, 1]
    print(checkPossibility(nums))
