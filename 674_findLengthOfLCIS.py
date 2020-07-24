# -*- coding: utf-8 -*-

"""
Created on 2020-06-22 23:48
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def findLengthOfLCIS(nums):
    if not nums or len(nums) < 1:
        return 0
    tmp = [1] * len(nums)
    for idx in range(1, len(nums)):
        if nums[idx] > nums[idx-1]:
            tmp[idx] = tmp[idx-1] + 1
    return max(tmp)

if __name__ == '__main__':
    test1 = [1, 3, 5, 4, 7]
    # test2 = [2, 2, 2, 2, 2]
    # test3 = [1, 3, 5, 7]
    test4 = []
    print(findLengthOfLCIS(test1))
    # print(findLengthOfLCIS(test2))
    # print(findLengthOfLCIS(test3))
    print(findLengthOfLCIS(test4))
