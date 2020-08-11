# -*- coding: utf-8 -*-

"""
Created on 2020-08-11 20:16
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def findMaxConsecutiveOnes(nums):
    cnt = 0
    max_cnt = 0
    for num in nums:
        if num == 1:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 0
    return max(max_cnt, cnt)


if __name__ == '__main__':
    test1 = [1,1,0,1,1,1]
    print(findMaxConsecutiveOnes(test1))