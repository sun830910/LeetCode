# -*- coding: utf-8 -*-

"""
Created on 1/22/21 4:08 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def game(guess, answer):
    result = 0
    for idx in range(3):
        if guess[idx] == answer[idx]:
            result += 1
    return result


if __name__ == '__main__':
    guess = [1, 2, 3]
    answer = [1, 2, 3]
    print(game(guess, answer))
    guess = [2, 2, 3]
    answer = [3, 2, 1]
    print(game(guess, answer))
