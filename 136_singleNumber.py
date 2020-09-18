# -*- coding: utf-8 -*-

"""
Created on 2020-09-18 16:44
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def singleNumber(nums):
    for idx in range(len(nums)):
        if idx == 0:
            res = nums[idx]
        else:
            res ^= nums[idx]
    return res


def singleNumber_bad(nums):
    cnt = list()
    for num in nums:
        if num not in cnt:
            cnt.append(num)
        else:
            cnt.remove(num)
    if len(cnt) == 1:
        return cnt[0]
    else:
        return 0

if __name__ == '__main__':
    test = [2, 2, 1]
    print(singleNumber(test))

    test = [4, 1, 2, 1, 2]
    print(singleNumber(test))