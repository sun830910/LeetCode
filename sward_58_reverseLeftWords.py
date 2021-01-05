# -*- coding: utf-8 -*-

"""
Created on 1/5/21 5:15 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def reverseLeftWords(s, n):
    return s[n:] + s[:n]


if __name__ == '__main__':
    s = "abcdefg"
    k = 2
    print(reverseLeftWords(s, k))  # "cdefgab"
    s = "lrloseumgh"
    k = 6
    print(reverseLeftWords(s, k))  # "umghlrlose"
