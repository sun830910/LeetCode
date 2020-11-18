# -*- coding: utf-8 -*-

"""
Created on 2020-11-18 11:16
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def addStrings(num1, num2):
    idx1 = len(num1) - 1
    idx2 = len(num2) - 1
    toNext = 0
    result = ""
    while idx1 >= 0 and idx2 >= 0:
        current = int(num1[idx1]) + int(num2[idx2]) + toNext
        toNext = current // 10
        result += str(current % 10)
        idx1 -= 1
        idx2 -= 1
    while idx1 >= 0:
        current = int(num1[idx1]) + toNext
        toNext = current // 10
        result += str(current % 10)
        idx1 -= 1
    while idx2 >= 0:
        current = int(num2[idx2]) + toNext
        toNext = current // 10
        result += str(current % 10)
        idx2 -= 1
    if toNext != 0:
        result += str(toNext)
    return result[::-1]


if __name__ == '__main__':
    # num1 = "123"
    # num2 = "123"
    # print(addStrings(num1, num2))
    # num1 = "99"
    # num2 = "1"
    # print(addStrings(num1, num2))
    num1 = "9133"
    num2 = "0"
    print(addStrings(num1, num2))
