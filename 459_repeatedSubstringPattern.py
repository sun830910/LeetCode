# -*- coding: utf-8 -*-

"""
Created on 2020-11-18 13:55
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

#  40%
def repeatedSubstringPattern(s):
    if not s:
        return False
    S = len(s)
    if S == 1:
        return False
    for idx in range(1, S):
        tmp = s[:idx]
        N = len(tmp)
        if S % N == 0 and tmp * (S // N) == s:
            return True
    return False


if __name__ == '__main__':
    s = "abab"
    print(repeatedSubstringPattern(s))
    s = "aba"
    print(repeatedSubstringPattern(s))
    s = "abcabcabcabc"
    print(repeatedSubstringPattern(s))
    s = "ababab"
    print(repeatedSubstringPattern(s))
