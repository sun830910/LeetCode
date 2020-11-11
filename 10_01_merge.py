# -*- coding: utf-8 -*-

"""
Created on 2020-11-11 14:58
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def merge(A, m, B, n):
    a_idx = m - 1
    b_idx = n - 1
    current_idx = m + n - 1
    while a_idx >= 0 and b_idx >= 0:
        if A[a_idx] >= B[b_idx]:
            A[current_idx] = A[a_idx]
            a_idx -= 1
        else:
            A[current_idx] = B[b_idx]
            b_idx -= 1
        current_idx -= 1

    if b_idx >= 0:
        A[:current_idx + 1] = B[:b_idx + 1]
    return A


if __name__ == '__main__':
    A = [1, 2, 3, 0, 0, 0]
    m = 3
    B = [2, 5, 6]
    n = 3
    print(merge(A, m, B, n))

    A = [0]
    m = 0
    B = [1]
    n = 1
    print(merge(A, m, B, n))

    A = [1, 0]
    m = 1
    B = [2]
    n = 1
    print(merge(A, m, B, n))
