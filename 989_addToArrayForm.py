# -*- coding: utf-8 -*-

"""
Created on 2020-11-16 09:42
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def addToArrayForm(A, K):
    if not A:
        return []
    str_K = str(K)
    list_K = []
    for k in str_K:
        list_K.append(int(k))
    list_K = list_K[::-1]
    list_A = A[::-1]
    idx_A, idx_K = 0, 0
    result = []
    toNext = 0
    while idx_A < len(list_A) and idx_K < len(list_K):
        current = toNext + list_A[idx_A] + list_K[idx_K]
        toNext = current // 10
        result.append(current % 10)
        idx_A += 1
        idx_K += 1
    while idx_A < len(list_A):
        current = toNext + list_A[idx_A]
        toNext = current // 10
        result.append(current% 10)
        idx_A += 1
    while idx_K < len(list_K):
        current = toNext + list_K[idx_K]
        toNext = current // 10
        result.append(current% 10)
        idx_K += 1
    if toNext != 0:
        result.append(toNext)

    return result[::-1]


if __name__ == '__main__':
    A = [1, 2, 0, 0]
    K = 34
    print(addToArrayForm(A, K))
    A = [2, 7, 4]
    K = 181
    print(addToArrayForm(A, K))
    A = [2, 1, 5]
    K = 806
    print(addToArrayForm(A, K))
    A = [9, 9]
    K = 1
    print(addToArrayForm(A, K))

    A = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
    K = 1
    print(addToArrayForm(A, K))

    A = [0]
    K = 23
    print(addToArrayForm(A, K))