# -*- coding: utf-8 -*-

"""
Created on 2020-06-23 23:11
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def replaceElements(arr):
    right_max = arr[-1]
    for idx in range(len(arr)-1, 0, -1):
        # 存一下目前指针的数
        tmp = arr[idx]
        # 取代一下目前的数
        arr[idx] = right_max
        # 看一下要不要取代掉现在的最大值
        right_max = max(right_max, tmp)
    arr[0] = right_max
    arr[-1] = -1
    return arr
if __name__ == '__main__':
    print(replaceElements([17,18,5,4,6,1]))