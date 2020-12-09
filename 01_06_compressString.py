# -*- coding: utf-8 -*-

"""
Created on 12/9/20 5:06 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def compressString(S):
    if not S:
        return ""
    current = S[0]
    counter = 1
    length = len(S)
    idx = 1
    result = ""
    while idx < length:
        if S[idx] == current:
            counter += 1
        else:
            result += current
            result += str(counter)
            current = S[idx]
            counter = 1
        idx += 1
    result += current
    result += str(counter)
    if len(result) >= length:
        return S
    return result


if __name__ == '__main__':
    S = "aabcccccaaa"
    print(compressString(S))  # "a2b1c5a3"
    S = "abbccd"
    print(compressString(S))  # "abbccd"
    S = ""
    print(compressString(S))
    S = "a"
    print(compressString(S))
