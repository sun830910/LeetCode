# -*- coding: utf-8 -*-

"""
Created on 11/19/20 6:25 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def canPermutePalindrome(s):
    if not s or len(s) < 1:
        return False
    record = dict()
    for idx in s:
        if idx not in record:
            record.setdefault(idx, 1)
        else:
            record[idx] += 1
    cnt = 0
    for key in record:
        if record.get(key) % 2 == 1:
            cnt += 1
        if cnt > 1:
            return False
    return True


if __name__ == '__main__':
    s = "tactcoa"
    print(canPermutePalindrome(s))
    s = "as"
    print(canPermutePalindrome(s))
