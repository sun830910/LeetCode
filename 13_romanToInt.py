# -*- coding: utf-8 -*-

"""
Created on 2020-09-13 21:01
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def romanToInt(s):
    Roman2Int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for idx in range(len(s)-1):
        if Roman2Int[s[idx]] < Roman2Int[s[idx + 1]]:
            result -= Roman2Int[s[idx]]
        else:
            result += Roman2Int[s[idx]]
    return result + Roman2Int[s[-1]]

if __name__ == '__main__':
    s = "III"
    print(romanToInt(s))
    s = "IV"
    print(romanToInt(s))
