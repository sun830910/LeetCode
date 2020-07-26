# -*- coding: utf-8 -*-

"""
Created on 2020-07-24 23:42
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def thirdMax(nums):
    tmps = list(set(nums))
    if len(tmps) < 3:
        return max(tmps)
    tmps.sort()
    return tmps[-3]

def best_thirdMax(nums):
    first, second, third = -float('inf'), -float('inf'), -float('inf')
    for num in nums:
        if num > first:
            first, second, third = num, first, second
        elif num == first:
            continue
        elif num > second:
            second, third = num, second
        elif num == second:
            continue
        elif num > third:
            third = num
        else:
            pass

    if third != -float('inf'):
        return third
    else:
        return first


if __name__ == '__main__':

    test1 = [3, 2, 1]
    test2 = [1, 2]
    test3 = [2, 2, 3, 1]

    print(thirdMax(test1))
    print(thirdMax(test2))
    print(thirdMax(test3))

    print(best_thirdMax(test1))
    print(best_thirdMax(test2))
    print(best_thirdMax(test3))