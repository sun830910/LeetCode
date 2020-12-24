# -*- coding: utf-8 -*-

"""
Created on 12/24/20 2:40 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def bitwiseComplement(N):
    bin_N = bin(N)
    result = ""
    for idx in bin_N[2:]:
        if idx == "0":
            result += "1"
        else:
            result += "0"

    return int(result, 2)


if __name__ == '__main__':
    N = 5
    print(bitwiseComplement(N))
    N = 7
    print(bitwiseComplement(N))
    N = 10
    print(bitwiseComplement(N))
    N = 0
    print(bitwiseComplement(N))
