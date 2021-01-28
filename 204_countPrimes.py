# -*- coding: utf-8 -*-

"""
Created on 1/28/21 9:02 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def countPrimes(n):
    is_prime = [True] * n
    cnt = 0
    for idx in range(2, int(pow(n, 0.5)) + 1):  # 从2开始就行，因为0和1都不是质数
        if is_prime[idx]:  # 若碰到质数
            for j in range(idx * idx, n, idx):
                is_prime[j] = False
    for idx in range(2, n):
        if is_prime[idx]:
            cnt += 1
    return cnt


if __name__ == '__main__':
    n = 10
    print(countPrimes(n))
    n = 0
    print(countPrimes(n))
    n = 1
    print(countPrimes(n))
