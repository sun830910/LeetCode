# -*- coding: utf-8 -*-

"""
Created on 11/25/20 5:55 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def getSum(a, b):
    # 2^32
    MASK = 0x100000000
    # 整型最大值
    MAX_INT = 0x7FFFFFFF
    MIN_INT = MAX_INT + 1
    while b != 0:
        # 计算进位
        carry = (a & b) << 1
        # 取余范围限制在 [0, 2^32-1] 范围内
        a = (a ^ b) % MASK
        b = carry % MASK
    return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)


if __name__ == '__main__':
    a = 1
    b = 2
    print(getSum(a, b))
