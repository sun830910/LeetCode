# -*- coding: utf-8 -*-

"""
Created on 2020-08-11 20:40
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def findPairs(nums, k):
    result = 0
    cnt_dict = dict()
    for num in nums:
        if num in cnt_dict:
            cnt_dict[num] += 1
        else:
            cnt_dict.setdefault(num, 1)

    for idx in cnt_dict:
        if (k > 0 and idx + k in cnt_dict) or (k == 0 and cnt_dict[idx] > 1):
            result += 1
    return result

if __name__ == '__main__':
    # test1 = [3, 1, 4, 1, 5]
    # k = 2
    # print(findPairs(test1, k))
    #
    # test2 = [1, 2, 3, 4, 5]
    # k = 1
    # print(findPairs(test2, k))

    test3 = [1,3,1,5,4]
    k = 0
    print(findPairs(test3, k))

