# -*- coding: utf-8 -*-

"""
Created on 2020-11-16 15:23
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def romanToInt(s):
    if not s:
        return 0
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for idx in range(len(s)-1):
        if roman_dict.get(s[idx]) < roman_dict.get(s[idx+1]):
            result -= roman_dict.get(s[idx])
        else:
            result += roman_dict.get(s[idx])
    result += roman_dict.get(s[-1])
    return result

if __name__ == '__main__':
    s = "III"
    print(romanToInt(s))
    s = "IV"
    print(romanToInt(s))
    s = "IX"
    print(romanToInt(s))
    s = "LVIII"
    print(romanToInt(s))
    s = "MCMXCIV"
    print(romanToInt(s))
