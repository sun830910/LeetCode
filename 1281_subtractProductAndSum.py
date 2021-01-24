# -*- coding: utf-8 -*-

"""
Created on 1/24/21 4:43 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def subtractProductAndSum(n):
    sum_result = 0
    time_result = 1
    while n:
        current = n % 10
        sum_result += current
        time_result *= current
        n //= 10
    return time_result - sum_result


if __name__ == '__main__':
    n = 234
    print(subtractProductAndSum(n))
    n = 4421
    print(subtractProductAndSum(n))
