# -*- coding: utf-8 -*-

"""
Created on 2020-06-21 23:57
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def twoSum(numbers, target):
    done = {}
    for idx in range(len(numbers)):
        if (target-numbers[idx]) in done:
            return [done.get(target-numbers[idx])+1, idx+1]
        else:
            done[numbers[idx]] = idx
    return []

if __name__ == '__main__':
    print(twoSum([2, 7, 11, 15], 9))
    print(twoSum([2, 7, 11, 15], 4))