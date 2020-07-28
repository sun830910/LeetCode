# -*- coding: utf-8 -*-

"""
Created on 2020-07-28 23:11
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def minTimeToVisitAllPoints(points):
    if len(points) < 2:
        return 0
    result = 0
    for idx in range(len(points)-1):
        result += max(abs(points[idx+1][0] - points[idx][0]), abs(points[idx+1][1] - points[idx][1]))
    return result

if __name__ == '__main__':
    test1 = [[1, 1], [3, 4], [-1, 0]]
    test2 = [[3,2],[-2,2]]
    print(minTimeToVisitAllPoints(test1))
    print(minTimeToVisitAllPoints(test2))