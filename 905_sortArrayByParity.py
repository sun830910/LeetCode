# -*- coding: utf-8 -*-

"""
Created on 2020-08-26 20:53
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def sortArrayByParity(A):
    odd_idx = len(A)-1
    even_idx = 0
    while even_idx < odd_idx:
        while A[even_idx] % 2 == 0 and even_idx < odd_idx:  # 非偶数
            even_idx += 1
        while A[odd_idx] % 2 == 1 and even_idx < odd_idx:
            odd_idx -= 1
        A[odd_idx], A[even_idx] = A[even_idx], A[odd_idx]
    return A

if __name__ == '__main__':
    test = [3,1,2,4]
    print(sortArrayByParity(test))