# -*- coding: utf-8 -*-

"""
Created on 2020-11-14 10:18
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def largeGroupPositions(s):
    result = []
    if not s:
        return result
    start = 0
    end = 1
    while end < len(s):
        if s[start] == s[end]:
            end += 1
        else:
            if end - 1 - start >= 2:
                result.append([start, end - 1])
            start = end
    if end - start >= 3:
        result.append([start, end - 1])
    return result


if __name__ == '__main__':
    s = "abbxxxxzzy"
    print(largeGroupPositions(s))  # [[3,6]]

    s = "abc"
    print(largeGroupPositions(s))  # []

    s = "abcdddeeeeaabbbcd"
    print(largeGroupPositions(s))  # [[3,5],[6,9],[12,14]]

    s = "aaa"
    print(largeGroupPositions(s))

    s = "xaaa"
    print(largeGroupPositions(s))

    s = "aaax"
    print(largeGroupPositions(s))