# -*- coding: utf-8 -*-

"""
Created on 2020-11-14 18:34
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def minCostClimbingStairs(cost):
    if not cost or len(cost) < 2:
        return 0
    result = [0] * len(cost)
    result[0] = cost[0]
    result[1] = cost[1]
    for idx in range(2, len(cost)):
        result[idx] = min(result[idx - 1] + cost[idx], result[idx - 2] + cost[idx])
    return min(result[-1], result[-2])


if __name__ == '__main__':
    cost = [10, 15, 20]
    print(minCostClimbingStairs(cost))
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(minCostClimbingStairs(cost))
