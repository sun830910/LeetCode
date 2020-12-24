# -*- coding: utf-8 -*-

"""
Created on 12/24/20 3:07 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def convertToTitle(n):
    result = ""
    if n == 0:
        return result
    while n:
        n, remainder = divmod(n, 26)

        if remainder == 0:
            n -= 1
            remainder = 26
        result += chr(64 + remainder)

    return result[::-1]


if __name__ == '__main__':
    n = 1
    print(convertToTitle(n))  # A

    n = 28
    print(convertToTitle(n))  # AB

    n = 701
    print(convertToTitle(n))  # ZY

    n = 0
    print(convertToTitle(n))

    n = 26
    print(convertToTitle(n))  # Z

    n = 52
    print(convertToTitle(n))  # AZ

    n = 703
    print(convertToTitle(n))  # AAA
