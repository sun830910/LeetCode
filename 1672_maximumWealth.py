# -*- coding: utf-8 -*-

"""
Created on 1/11/21 5:21 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def maximumWealth(accounts):
    total = []
    for arr in accounts:
        total.append(sum(arr))
    return max(total)


if __name__ == '__main__':
    accounts = [[1, 2, 3], [3, 2, 1]]
    print(maximumWealth(accounts))
    accounts = [[1, 5], [7, 3], [3, 5]]
    print(maximumWealth(accounts))
