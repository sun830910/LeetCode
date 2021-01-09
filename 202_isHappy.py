# -*- coding: utf-8 -*-

"""
Created on 1/9/21 6:12 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def isHappy(n):
    record = set()
    while n != 1 and n not in record:
        record.add(n)
        next_num = 0
        while n != 0 :
            next_num += (n % 10) ** 2
            n = n // 10
        n = next_num
    return n == 1



if __name__ == '__main__':
    n = 19
    print(isHappy(n))
