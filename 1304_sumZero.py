# -*- coding: utf-8 -*-

"""
Created on 12/1/20 5:43 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

import random


# 废弃， 概率出错
# def sumZero(n):
#     if n == 0:
#         return []
#     if n == 1:
#         return [0]
#     record = dict()
#     while len(record.keys()) < n - 1:
#         ran = random.randint(-1000, 1000)
#         while ran in record:
#             ran = random.randint(-1000, 1000)
#         record.setdefault(ran, 1)
#     helper = sum(record.keys())
#     result = [num for num in record.keys()]
#     result.append((-1) * helper)  # 这步会有问题的，有可能会重复
#     return result

def sumZero(n):
    if n == 1:
        return [0]
    pos = [idx for idx in range(1, 1000)]
    neg = [(-1) * idx for idx in range(1, 1000)]
    result = []
    if n % 2 == 1:
        result.append(0)
    need = n // 2
    for idx in range(need):
        result.append(pos[idx])
        result.append(neg[idx])
    return result



if __name__ == '__main__':
    n = 1
    print(sumZero(n))
    n = 2
    print(sumZero(n))
    n = 3
    print(sumZero(n))
    n = 4
    print(sumZero(n))
    n = 5
    print(sumZero(n))
