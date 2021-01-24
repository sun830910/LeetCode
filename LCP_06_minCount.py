# -*- coding: utf-8 -*-

"""
Created on 1/23/21 2:12 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def minCount(coins):
    result = 0
    if not coins:
        return result
    for idx in range(len(coins)):
        num = coins[idx]
        quotient, remainder = divmod(num, 2)
        result += quotient
        result += remainder
    return result


if __name__ == '__main__':
    coins = [4, 2, 1]
    print(minCount(coins))
    coins = [2, 3, 10]
    print(minCount(coins))
