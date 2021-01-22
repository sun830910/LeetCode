# -*- coding: utf-8 -*-

"""
Created on 1/22/21 4:48 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def countConsistentStrings(allowed, words):
    result = 0
    if not allowed or not words:
        return result
    for word in words:
        word_set = set(word)
        jump_flag = False
        for vocab in word_set:
            if vocab not in allowed:
                jump_flag = True
            if jump_flag:
                break
        if not jump_flag:
            result += 1
    return result


if __name__ == '__main__':
    allowed = "ab"
    words = ["ad", "bd", "aaab", "baa", "badab"]
    print(countConsistentStrings(allowed, words))
    allowed = "abc"
    words = ["a", "b", "c", "ab", "ac", "bc", "abc"]
    print(countConsistentStrings(allowed, words))
    allowed = "cad"
    words = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]
    print(countConsistentStrings(allowed, words))
