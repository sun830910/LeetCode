# -*- coding: utf-8 -*-

"""
Created on 2020-09-16 17:31
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def reverse(x):
    str_x = str(x)
    if str_x[0] == '-':
        x = int('-' + str_x[1:][::-1])
    else:
        x = int(str_x[::-1])
    return x if -2147483648 < x < 2147483647 else 0


if __name__ == '__main__':
    test = 123
    print(reverse(test))
    test = -123
    print(reverse(test))
    test = 120
    print(reverse(test))
    test = 1534236469
    print(reverse(test))
