# -*- coding: utf-8 -*-

"""
Created on 2020-08-05 23:56
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def findShortestSubArray(nums):
    tmps = dict()
    for num in nums:
        if num not in tmps:
            tmps.setdefault(num, 1)
        else:
            tmps[num] += 1

    max_cnt = max(tmps.values())
    if max_cnt == 1:
        return 1

    target_nums = []
    for tmp in tmps:
        if tmps.get(tmp) == max_cnt:
            target_nums.append(tmp)

    start_idx, end_idx = 0, 0
    num_length = []
    for target_num in target_nums:
        flag = 1
        for idx in range(len(nums)):
            if nums[idx] == target_num:
                end_idx = idx
            if flag == 1:
                if nums[idx] == target_num:
                    start_idx = idx
                    flag -= 1
        num_length.append(end_idx-start_idx+1)
    return min(num_length)

if __name__ == '__main__':
    test1 = [1, 2, 2, 3, 1]
    print(findShortestSubArray(test1))