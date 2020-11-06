# -*- coding: utf-8 -*-

"""
Created on 2020-11-06 17:23
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def fib(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    return fib(N - 1) + fib(N - 2)

if __name__ == '__main__':
    for idx in range(31):
        print(fib(idx))
