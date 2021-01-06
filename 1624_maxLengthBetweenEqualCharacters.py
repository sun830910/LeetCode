# -*- coding: utf-8 -*-

"""
Created on 1/6/21 4:32 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def maxLengthBetweenEqualCharacters(s):
    record = dict()
    for idx in range(len(s)):
        vocab = s[idx]
        if vocab not in record:
            record.setdefault(vocab, [idx])
        else:
            record[vocab].append(idx)
    result = -1
    for val in record.values():
        if len(val) >= 2:
            result = max(result, max(val) - min(val) - 1)
    return result


if __name__ == '__main__':
    s = "aa"
    print(maxLengthBetweenEqualCharacters(s))
    s = "abca"
    print(maxLengthBetweenEqualCharacters(s))
    s = "cbzxy"
    print(maxLengthBetweenEqualCharacters(s))
    s = "cabbac"
    print(maxLengthBetweenEqualCharacters(s))
