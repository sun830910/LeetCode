# -*- coding: utf-8 -*-

"""
Created on 2020-11-18 10:22
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def firstUniqChar(s):
    record = dict()
    duplicate = dict()
    for idx, word in enumerate(s):
        if word in duplicate:
            continue
        elif word not in record and word not in duplicate:
            record[word] = idx
        elif word in record and word not in duplicate:
            record.pop(word)
            duplicate[word] = 1
    if len(record) == 0:
        return -1
    result = sorted(record, key=lambda x: record.get(x))
    return record.get(result[0])


if __name__ == '__main__':
    s = "leetcode"
    print(firstUniqChar(s))  # 0
    s = "loveleetcode"
    print(firstUniqChar(s))  # 2
    s = "aadadaad"
    print(firstUniqChar(s))  # -1
