# -*- coding: utf-8 -*-

"""
Created on 2020-07-28 23:58
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def checkIfExist(arr):
    Hash = {}
    for arr_idx in arr:
        print(Hash.get(arr_idx, 0)) # 自Hash中取key==3的值，不然就返回零
        Hash[arr_idx] = Hash.get(arr_idx, 0) + 1
    for arr_idx in arr:
        # 若arr_idx*2在Hash中不为空
        if Hash.get(arr_idx*2) is not None:
            # 若arr_idx为零
            if arr_idx * 2 == 0:
                # 若有两个以上的零则对
                if Hash.get(0) > 1:
                    return True
            else:
                return True
    return False

if __name__ == '__main__':
    arr1 = [10, 2, 5, 3]
    arr2 = [7, 1, 14, 11]
    arr3 = [3, 1, 7, 11]
    print(checkIfExist(arr1))
    # print(checkIfExist(arr2))
    # print(checkIfExist(arr3))