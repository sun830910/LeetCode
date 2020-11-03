# -*- coding: utf-8 -*-

"""
Created on 2020-11-03 20:47
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def twoSum(numbers, target):
    note = dict()
    for idx, num in enumerate(numbers):
        if target - num not in note:
            note.setdefault(num, idx)
        else:
            return [note.get(target-num)+1, idx+1]
    return []


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    print(twoSum(numbers, target))
