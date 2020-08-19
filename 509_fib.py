# -*- coding: utf-8 -*-

"""
Created on 2020-08-19 09:58
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
"""

def fib(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    return fib(N-1)+fib(N-2)

if __name__ == '__main__':
    print(fib(0))
    print(fib(1))
    print(fib(2))
    print(fib(3))
