# -*- coding: utf-8 -*-

"""
Created on 12/2/20 11:00 AM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


# 40%
def countLargestGroup(n):
    def get_position(num):
        str_num = str(num)
        total = 0
        for idx in range(len(str_num)):
            total += int(str_num[idx])
        return total

    heap = dict()
    for idx in range(1, n + 1):
        position = get_position(idx)
        if position not in heap:
            heap.setdefault(position, 1)
        else:
            heap[position] += 1
    max_value = max(heap.values())
    cnt = 0
    for key in heap:
        if heap.get(key) == max_value:
            cnt += 1
    return cnt


if __name__ == '__main__':
    n = 13
    print(countLargestGroup(n))  # 4
    n = 2
    print(countLargestGroup(n))  # 2
    n = 15
    print(countLargestGroup(n))  # 6
    n = 24
    print(countLargestGroup(n))  # 5
    n = 31
    print(countLargestGroup(n))  # 2
