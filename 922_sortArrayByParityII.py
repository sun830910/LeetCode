# -*- coding: utf-8 -*-

"""
Created on 2020-08-26 23:19
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def sortArrayByParityII(A):
    odd_idx = 1
    even_idx = 0
    while odd_idx < len(A) and even_idx < len(A):
        if A[odd_idx] % 2 == 0 and A[even_idx] % 2 == 1:
            A[odd_idx], A[even_idx] = A[even_idx], A[odd_idx]
        elif A[odd_idx] % 2 == 1:
            odd_idx += 2
        elif A[even_idx] % 2 == 0:
            even_idx += 2
    return A

if __name__ == '__main__':
    test = [5,2,7,4]
    print(sortArrayByParityII(test))

    test1 = [3,4]
    print(sortArrayByParityII(test1))