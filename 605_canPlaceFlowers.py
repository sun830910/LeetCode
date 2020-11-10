# -*- coding: utf-8 -*-

"""
Created on 2020-11-10 16:32
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def canPlaceFlowers(flowerbed, n):
    flowerbed.insert(0, 0)
    flowerbed.append(0)
    cnt = 0
    for idx in range(1, len(flowerbed) - 1):
        if flowerbed[idx - 1] == 0 and flowerbed[idx] == 0 and flowerbed[idx + 1] == 0:
            flowerbed[idx] = 1
            cnt += 1
    return cnt >= n


if __name__ == '__main__':
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    print(canPlaceFlowers(flowerbed, n))
    flowerbed = [1, 0, 0, 0, 1]
    n = 2
    print(canPlaceFlowers(flowerbed, n))