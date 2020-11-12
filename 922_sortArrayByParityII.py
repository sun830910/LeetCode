# -*- coding: utf-8 -*-

"""
Created on 2020-11-12 16:46
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def sortArrayByParityII(A):
    even_idx = 0
    odd_idx = 1
    length = len(A)  # 先将长度拉出来计算可以加速
    while even_idx < length and odd_idx < length:
        if A[even_idx] % 2 != 0 and A[odd_idx] % 2 != 1:
            A[odd_idx], A[even_idx] = A[even_idx], A[odd_idx]
        if A[even_idx] % 2 == 0:
            even_idx += 2
        if A[odd_idx] % 2 == 1:
            odd_idx += 2
    return A


if __name__ == '__main__':
    A = [4, 2, 5, 7]
    print(sortArrayByParityII(A))
    A = [0]
    print(sortArrayByParityII(A))
    A = [1, 1, 2, 2]
    print(sortArrayByParityII(A))
    A = []
    print(sortArrayByParityII(A))
