# -*- coding: utf-8 -*-

"""
Created on 2020-11-16 15:35
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def longestCommonPrefix(strs):
    result = ""
    if not strs:
        return result
    idx = 0
    min_length = min([len(word) for word in strs])
    stop = True
    while idx < min_length and stop:
        for word_idx in range(len(strs) - 1):
            if strs[word_idx][idx] != strs[word_idx + 1][idx]:
                stop = False
                break
        if stop == True:
            result += strs[0][idx]
        idx += 1
    return result


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    print(longestCommonPrefix(strs))
    strs = ["dog", "racecar", "car"]
    print(longestCommonPrefix(strs))
    strs = ["a"]
    print(longestCommonPrefix(strs))
