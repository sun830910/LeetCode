# -*- coding: utf-8 -*-

"""
Created on 2020-06-24 17:58
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def finalPrices(prices):
    stack = []
    res = prices
    for idx in range(len(prices)):
        while stack and prices[stack[-1]] >= prices[idx]:
            res[stack[-1]] -= prices[idx]
            stack.pop()
        stack.append(idx)
    return res

def finalPrices2(prices):
    result = prices
    stack = []
    for idx in range(len(prices)):
        while stack and prices[stack[-1]] >= prices[idx]:
            result[stack[-1]] -= prices[idx]
            stack.pop()
        stack.append(idx)
    return result

if __name__ == '__main__':
    test1 = [8,4,6,2,3]
    test2 = [1,2,3,4,5]
    test3 = [10,1,1,6]

    print(finalPrices(test1))
    print(finalPrices(test2))
    print(finalPrices(test3))
