# -*- coding: utf-8 -*-

"""
Created on 12/24/20 5:06 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def trailingZeroes(n):
    def factorial(num):
        if num == 0 or num == 1:
            return 1
        return num * factorial(num - 1)

    result = str(factorial(n))
    counter = 0
    for idx in range(len(result) - 1, -1, -1):
        if result[idx] == "0":
            counter += 1
        else:
            break
    return counter


if __name__ == '__main__':
    n = 3
    print(trailingZeroes(n))
    n = 5
    print(trailingZeroes(n))
