# -*- coding: utf-8 -*-

"""
Created on 11/20/20 3:48 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

import random


# 90%
def modifyString(s):
    vocabs = "abcdefghijklmnopqrstuvwxyz"
    s_list = list("_" + s + "_")
    for idx in range(1, len(s_list) - 1):
        if s_list[idx] == "?":
            vocab_idx = 0
            while vocabs[vocab_idx] in s_list[idx - 1: idx + 2]:
                vocab_idx = random.randint(0, len(vocabs) - 1)
            s_list[idx] = vocabs[vocab_idx]
    return "".join(s_list[1:-1])


# 40%
# def modifyString(s):
#     if not s:
#         return ""
#     vocabString = "abcdefghijklmnopqrstuvwxyz"
#     vocab_idx, s_idx = 0, 0
#     list_s = list('_' + s + '_')
#     while s_idx < len(list_s):
#         if list_s[s_idx] == "?":
#             while vocabString[vocab_idx] in list_s[s_idx - 1:s_idx + 2]:
#                 vocab_idx = random.randint(0, len(vocabString) - 1)
#
#             list_s[s_idx] = vocabString[vocab_idx]
#         s_idx += 1
#     return "".join(list_s[1:-1])


if __name__ == '__main__':
    s = "?za?s"
    print(modifyString(s))
    s = "?"
    print(modifyString(s))
    s = " "
    print(modifyString(s))
    s = "???"
    print(modifyString(s))
