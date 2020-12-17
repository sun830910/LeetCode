# -*- coding: utf-8 -*-

"""
Created on 12/17/20 6:55 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def checkRecord(s):
    if not s:
        return True
    a_cnt = 0
    if s[0] == 'A':
        a_cnt += 1
    if len(s) > 1 and s[-1] == 'A':
        a_cnt += 1
    if a_cnt > 1:
        return False
    idx = 1
    while idx < len(s) - 1:
        if s[idx] == 'A':
            a_cnt += 1
        if a_cnt > 1:
            return False
        if s[idx] == 'L':
            if s[idx-1] == s[idx+1] == s[idx]:
                return False
        idx += 1
    return True


if __name__ == '__main__':
    s = "PPALLP"
    print(checkRecord(s))
    s = "PPALLL"
    print(checkRecord(s))
    s = ""
    print(checkRecord(s))
    s = "A"
    print(checkRecord(s))