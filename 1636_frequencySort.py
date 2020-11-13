# -*- coding: utf-8 -*-

"""
Created on 2020-11-13 18:24
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def frequencySort(nums):
    result = []
    if not nums:
        return result
    num2count = dict()
    for num in nums:
        if num not in num2count:
            num2count.setdefault(num, 1)
        else:
            num2count[num] += 1
    num2count = sorted(num2count.items(), key=lambda x: (x[1], -x[0]))  # 注意这里sort的用法，取-x[0]取逆序
    for idx in range(len(num2count)):
        result += [num2count[idx][0] for _ in range(num2count[idx][1])]
    return result


if __name__ == '__main__':
    nums = [1, 1, 2, 2, 2, 3]
    print(frequencySort(nums))  # [3,1,1,2,2,2]
    nums = [2, 3, 1, 3, 2]
    print(frequencySort(nums))  # [1,3,3,2,2]
    nums = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
    print(frequencySort(nums))  # [5,-1,4,4,-6,-6,1,1,1]
