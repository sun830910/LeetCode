# -*- coding: utf-8 -*-

"""
Created on 12/1/20 4:20 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def numPairsDivisibleBy60(time):
    heap = dict()
    result = 0
    for idx in range(60):
        heap.setdefault(idx, 0)
    for song in time:
        which_heap = song % 60
        heap[which_heap] += 1
    for key in range(1, 30):
        result += heap.get(key) * heap.get(60 - key)
    result += heap.get(30) * (heap.get(30) - 1) // 2
    result += heap.get(0) * (heap.get(0) - 1) // 2
    return result


if __name__ == '__main__':
    time = [30, 20, 150, 100, 40]
    print(numPairsDivisibleBy60(time))
    time = [60, 60, 60]
    print(numPairsDivisibleBy60(time))
