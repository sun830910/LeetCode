# -*- coding: utf-8 -*-

"""
Created on 2020-08-24 19:12
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def merge(A, m, B, n):
    idx1 = m - 1
    idx2 = n - 1
    current_idx = m + n - 1
    while idx1 > -1 and idx2 > -1:
        if B[idx2] > A[idx1]:
            A[current_idx] = B[idx2]
            current_idx -= 1
            idx2 -= 1
        else:
            A[current_idx] = A[idx1]
            current_idx -= 1
            idx1 -= 1
    if idx2 != -1:
        A[:idx2+1] = B[:idx2 + 1]  # 比较完B还有剩下的，全填到A前面即可
    return A

if __name__ == '__main__':
    A = [1, 2, 3, 0, 0, 0]
    m = 3
    B = [2, 5, 6]
    n = 3
    print(merge(A, m, B, n))