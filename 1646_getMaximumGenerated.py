# -*- coding: utf-8 -*-

"""
Created on 2020-11-13 16:54
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def getMaximumGenerated(n):
    result = [0] * (n + 1)
    if n >= 0:
        result[0] = 0
    if n >= 1:
        result[1] = 1
    if n >= 2:
        for idx in range(2, len(result)):
            if idx % 2 == 0:  # 偶数
                result[idx] = result[idx // 2]
            else:
                result[idx] = result[idx // 2] + result[idx // 2 + 1]
    return max(result)


if __name__ == '__main__':
    n = 7
    print(getMaximumGenerated(n))
    n = 2
    print(getMaximumGenerated(n))
    n = 3
    print(getMaximumGenerated(n))
    n = 0
    print(getMaximumGenerated(n))
    n = 1
    print(getMaximumGenerated(n))
