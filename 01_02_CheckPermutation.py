# -*- coding: utf-8 -*-

"""
Created on 2020-11-13 14:45
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def CheckPermutation(s1, s2):
    if len(s1) != len(s2) or len(set(s1)) != len(set(s2)):
        return False
    record1 = dict()
    record2 = dict()
    for idx in range(len(s1)):
        if s1[idx] not in record1:
            record1.setdefault(s1[idx], 1)
        else:
            record1[s1[idx]] += 1
        if s2[idx] not in record2:
            record2.setdefault(s2[idx], 1)
        else:
            record2[s2[idx]] += 1
    for record_idx in record1:
        if record_idx not in record2:
            return False
        if record1.get(record_idx) != record2.get(record_idx):
            return False
    return True



if __name__ == '__main__':
    s1 = "abc"
    s2 = "bca"
    print(CheckPermutation(s1, s2))
    s1 = "abc"
    s2 = "bad"
    print(CheckPermutation(s1, s2))