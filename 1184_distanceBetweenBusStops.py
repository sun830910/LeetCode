# -*- coding: utf-8 -*-

"""
Created on 2020-08-09 12:02
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def distanceBetweenBusStops(distance, start, destination):
    # 若起点坐标大于终点坐标，如
   if start < destination:
       return min(sum(distance[start:destination]), sum(distance[0:start] + distance[destination:]))
   else:
       return min(sum(distance[destination:start]), sum(distance[0:destination] + distance[start:]))

if __name__ == '__main__':
    # 1
    distance = [1, 2, 3, 4]
    start = 0
    destination = 1

    # 3
    # distance = [1, 2, 3, 4]
    # start = 2
    # destination = 0

    # 4
    # distance = [1, 2, 3, 4]
    # start = 0
    # destination = 3
    print(distanceBetweenBusStops(distance, start, destination))
