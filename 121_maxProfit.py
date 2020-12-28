# -*- coding: utf-8 -*-

"""
Created on 12/28/20 7:27 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def maxProfit(prices):
    min_price = float("inf")
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices))
    prices = [7, 6, 4, 3, 1]
    print(maxProfit(prices))
