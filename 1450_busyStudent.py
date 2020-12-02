# -*- coding: utf-8 -*-

"""
Created on 12/2/20 10:07 AM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def busyStudent(startTime, endTime, queryTime):
    length = len(startTime)
    if length != len(endTime) != len(queryTime):
        return
    cnt = 0
    idx = 0
    while idx < length:
        if startTime[idx] <= queryTime <= endTime[idx]:
            cnt += 1
        idx += 1
    return cnt


if __name__ == '__main__':
    startTime = [1, 2, 3]
    endTime = [3, 2, 7]
    queryTime = 4
    print(busyStudent(startTime, endTime, queryTime))

    startTime = [4]
    endTime = [4]
    queryTime = 4
    print(busyStudent(startTime, endTime, queryTime))

    startTime = [4]
    endTime = [4]
    queryTime = 5
    print(busyStudent(startTime, endTime, queryTime))

    startTime = [1, 1, 1, 1]
    endTime = [1, 3, 2, 4]
    queryTime = 7
    print(busyStudent(startTime, endTime, queryTime))

    startTime = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    endTime = [10, 10, 10, 10, 10, 10, 10, 10, 10]
    queryTime = 5
    print(busyStudent(startTime, endTime, queryTime))
