# -*- coding: utf-8 -*-

"""
Created on 1/19/21 1:37 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     if n >= 2:
#         return (fib(n - 1) + fib(n - 2)) % 1000000007


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        """
        _ = 0时，a = 1 ， b = 1，若n<1时并不会进入回圈
        _ = 1时，a = 1 ， b = 2，a的值等价于fib(2)
        _ = 2时，a = 2 ， b = 3，a的值等价于fib(3)
        _ = 3时，a = 3 ， b = 5，a的值等价于fib(4)
        _ = 4时，a = 5 ， b = 8，a的值等价于fib(5)
        """
        a, b = b, a + b
    return a % 1000000007


if __name__ == '__main__':
    n = 2
    # print(fib(n))
    n = 5
    print(fib(n))
