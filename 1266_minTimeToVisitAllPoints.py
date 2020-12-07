# -*- coding: utf-8 -*-

"""
Created on 12/7/20 2:15 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def minTimeToVisitAllPoints(points):
    def compute_time(point1, point2):
        point1_x = point1[0]
        point1_y = point1[1]
        point2_x = point2[0]
        point2_y = point2[1]
        return max(abs(point1_x - point2_x), abs(point1_y - point2_y))
    if not points:
        return
    time = 0
    idx = 0
    while idx < len(points) - 1:
        time += compute_time(points[idx], points[idx + 1])
        idx += 1
    return time


if __name__ == '__main__':
    points = [[1, 1], [3, 4], [-1, 0]]
    print(minTimeToVisitAllPoints(points))
    points = [[3, 2], [-2, 2]]
    print(minTimeToVisitAllPoints(points))
