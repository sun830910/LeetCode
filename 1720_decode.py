# -*- coding: utf-8 -*-

"""
Created on 1/22/21 5:05 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def decode(encoded, first):
    length = len(encoded)
    arr = [first] + [0] * length
    for idx in range(length):
        arr[idx + 1] = arr[idx] ^ encoded[idx]
    return arr


if __name__ == '__main__':
    encoded = [1, 2, 3]
    first = 1
    print(decode(encoded, first))
    encoded = [6, 2, 7, 3]
    first = 4
    print(decode(encoded, first))
