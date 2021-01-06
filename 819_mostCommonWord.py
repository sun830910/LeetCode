# -*- coding: utf-8 -*-

"""
Created on 1/6/21 2:52 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

import re


def mostCommonWord(paragraph, banned):
    arr = paragraph.strip().split()
    record = dict()
    for word in arr:
        word = re.findall(r'[a-z]+', word.lower())[0]
        if word not in record:
            record.setdefault(word, 1)
        else:
            record[word] += 1
    for word in banned:
        record[word] = 0
    max_cnt = max(record.values())
    for key, val in record.items():
        if val == max_cnt:
            return key
    return


if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print(mostCommonWord(paragraph, banned))
