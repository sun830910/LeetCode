# -*- coding: utf-8 -*-

"""
Created on 11/30/20 2:05 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def sortArrayByParity(A):
    if not A:
        return
    odd = 0
    even = len(A) - 1
    while odd < even:
        while A[odd] % 2 == 0 and odd < even:
            odd += 1
        while A[even] % 2 == 1 and odd < even:
            even -= 1
        if A[odd] % 2 == 1 and A[even] % 2 == 0:
            A[odd], A[even] = A[even], A[odd]
            odd += 1
            even -= 1
    return A

if __name__ == '__main__':
    A = [3, 1, 2, 4]
    print(sortArrayByParity(A))
    A = [0,2]
    print(sortArrayByParity(A))