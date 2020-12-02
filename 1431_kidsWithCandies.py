# -*- coding: utf-8 -*-

"""
Created on 12/2/20 10:29 AM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def kidsWithCandies(candies, extraCandies):
    if not candies:
        return
    max_candies = max(candies)
    result = []
    for val in candies:
        if val + extraCandies >= max_candies:
            result.append(True)
        else:
            result.append(False)
    return result

if __name__ == '__main__':
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    print(kidsWithCandies(candies, extraCandies))

    candies = [4, 2, 1, 1, 2]
    extraCandies = 1
    print(kidsWithCandies(candies, extraCandies))

    candies = [12, 1, 12]
    extraCandies = 10
    print(kidsWithCandies(candies, extraCandies))

