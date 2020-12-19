# -*- coding: utf-8 -*-

"""
Created on 12/19/20 11:13 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def arrayStringsAreEqual(word1, word2):
    result1 = ""
    result2 = ""
    for idx in word1:
        result1 += idx
    for idx in word2:
        result2 += idx
    return result1 == result2


if __name__ == '__main__':
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    print(arrayStringsAreEqual(word1, word2))
    word1 = ["a", "cb"]
    word2 = ["ab", "c"]
    print(arrayStringsAreEqual(word1, word2))
    word1 = ["abc", "d", "defg"]
    word2 = ["abcddefg"]
    print(arrayStringsAreEqual(word1, word2))
