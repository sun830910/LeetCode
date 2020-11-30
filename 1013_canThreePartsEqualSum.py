# -*- coding: utf-8 -*-

"""
Created on 11/30/20 4:04 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def canThreePartsEqualSum(A):
    splited_sum = sum(A) / 3
    if splited_sum % 1 != 0:
        return False
    left_idx, right_idx = 1, len(A) - 2
    left_sum, right_sum = A[0], A[-1]
    while left_idx < len(A) - 2 and right_idx > 1:
        if left_sum == splited_sum and right_sum == splited_sum:
            break
        if left_sum != splited_sum:
            left_sum += A[left_idx]
            left_idx += 1
        if right_sum != splited_sum:
            right_sum += A[right_idx]
            right_idx -= 1
        if left_idx > right_idx:
            return False
    mid_sum = sum(A[left_idx:right_idx + 1])
    return left_sum == mid_sum == right_sum


if __name__ == '__main__':
    A = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]
    print(canThreePartsEqualSum(A))
    A = [0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]
    print(canThreePartsEqualSum(A))
