# -*- coding: utf-8 -*-

"""
Created on 1/21/21 8:26 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def numJewelsInStones(jewels, stones):
    result = 0
    if not jewels or not stones:
        return result
    for stone in stones:
        if stone in jewels:
            result += 1
    return result


if __name__ == '__main__':
    J = "aA"
    S = "aAAbbbb"
    print(numJewelsInStones(J, S))
    J = "z"
    S = "ZZ"
    print(numJewelsInStones(J, S))
