# -*- coding: utf-8 -*-

"""
Created on 2020-11-10 16:09
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def bubbleSort(A):
    for idx1 in range(len(A)):
        for idx2 in range(len(A) - idx1 - 1):
            if A[idx2] > A[idx2 + 1]:
                A[idx2], A[idx2 + 1] = A[idx2 + 1], A[idx2]
    return A


# def sortedSquares(A):
#     for idx, a in enumerate(A):
#         A[idx] = a * a
#     return bubbleSort(A)

def sortedSquares(A):
    result = [0] * len(A)
    left = 0
    right = len(A) - 1
    done = len(A) - 1
    while right >= left:
        right_num = A[right] * A[right]
        left_num = A[left] * A[left]
        if right_num > left_num:
            result[done] = right_num
            right -= 1
        else:
            result[done] = left_num
            left += 1
        done -= 1
    return result


if __name__ == '__main__':
    nums = [-4, -1, 0, 3, 10]
    print(sortedSquares(nums))

    nums = [-7, -3, 2, 3, 11]
    print(sortedSquares(nums))
