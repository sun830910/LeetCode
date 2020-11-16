# -*- coding: utf-8 -*-

"""
Created on 2020-11-16 17:37
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def addBinary(a, b):
    idx_a = len(a) - 1
    idx_b = len(b) - 1
    toNext = 0
    result = ""
    while idx_a >= 0 and idx_b >= 0:
        current = int(a[idx_a]) + int(b[idx_b]) + toNext
        toNext = current // 2
        result += str(current % 2)
        idx_a -= 1
        idx_b -= 1
    while idx_a >= 0:
        current = int(a[idx_a]) + toNext
        toNext = current // 2
        result += str(current % 2)
        idx_a -= 1

    while idx_b >= 0:
        current = int(b[idx_b]) + toNext
        toNext = current // 2
        result += str(current % 2)
        idx_b -= 1
    if toNext != 0:
        result += str(toNext)
    return result[::-1]


if __name__ == '__main__':
    a = "11"
    b = "1"
    print(addBinary(a, b))
    a = "1010"
    b = "1011"
    print(addBinary(a, b))

    a = "1"
    b = "0"
    print(addBinary(a, b))
