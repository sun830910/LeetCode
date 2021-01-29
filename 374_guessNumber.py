# -*- coding: utf-8 -*-

"""
Created on 1/29/21 4:17 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

pick = 1


def guess(num):
    if pick < num:
        return -1
    elif pick > num:
        return 1
    else:
        return 0


def guessNumber(n):
    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
        guess_result = guess(mid)
        if guess_result == 0:
            return mid
        elif guess_result == -1:
            right = mid
        else:
            left = mid + 1
    return


if __name__ == '__main__':
    print(guessNumber(1))
