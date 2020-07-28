# -*- coding: utf-8 -*-

"""
Created on 2020-07-28 23:23
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def canPlaceFlowers(flowerbed, n):
    flowerbed  = [0] + flowerbed
    flowerbed = flowerbed + [0]

    for idx in range(1, len(flowerbed)-1):
        if flowerbed[idx-1] == 0 and flowerbed[idx] == 0 and flowerbed[idx+1] == 0:
            n -= 1
            flowerbed[idx] = 1

    return n <= 0

if __name__ == '__main__':
    flowerbed1 = [1, 0, 0, 0, 1]
    n1 = 1
    flowerbed2 = [1, 0, 0, 0, 1]
    n2 = 2
    flowerbed3 = [1, 0, 0, 0, 0, 1]
    n3 = 2
    # print(canPlaceFlowers(flowerbed1, n1))
    # print(canPlaceFlowers(flowerbed2, n2))
    print(canPlaceFlowers(flowerbed3, n3))
