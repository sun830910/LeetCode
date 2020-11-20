# -*- coding: utf-8 -*-

"""
Created on 11/20/20 5:27 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def judgeCircle(moves):
    if not moves and len(moves) < 1:
        return False
    left_and_right = 0
    up_and_down = 0
    for value in moves:
        if value == "L":
            left_and_right += 1
        elif value == "R":
            left_and_right -= 1
        elif value == "U":
            up_and_down += 1
        elif value == "D":
            up_and_down -= 1
    return left_and_right == 0 and up_and_down == 0


if __name__ == '__main__':
    moves = "UD"
    print(judgeCircle(moves))
    moves = "LL"
    print(judgeCircle(moves))
