# -*- coding: utf-8 -*-

"""
Created on 2020-09-17 18:02
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def lengthOfLastWord(s):
    result = 0
    flag = False
    idx = len(s)-1
    while idx >= 0:
        while idx >= 0 and s[idx] != " ":
            flag = True
            result += 1
            idx -= 1
        idx -= 1
        if flag:
            break
    return result



if __name__ == '__main__':
    test = "Hello World"
    print(lengthOfLastWord(test))  # 5

    test = "Hello World  "
    print(lengthOfLastWord(test))  # 5

    # test = ""
    # print(lengthOfLastWord(test))  # 0

    test = "WQEGDSGFsdfwsdewt"
    print(lengthOfLastWord(test))  # 17

    test = "a"
    print(lengthOfLastWord(test))  # 1

    test = " "
    print(lengthOfLastWord(test))  # 0

    test = "  "
    print(lengthOfLastWord(test))  # 0