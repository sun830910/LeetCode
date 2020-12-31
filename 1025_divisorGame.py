# -*- coding: utf-8 -*-

"""
Created on 12/31/20 4:00 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def divisorGame(N):
    return N % 2 == 0


if __name__ == '__main__':
    N = 2
    print(divisorGame(N))
    N = 3
    print(divisorGame(N))
