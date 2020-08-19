# -*- coding: utf-8 -*-

"""
Created on 2020-08-19 10:10
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def matrixReshape(nums, r, c):
    if len(nums)*len(nums[0]) != r*c:
        return nums

    nums = [num for rows in nums for num in rows]
    result = [[0]*c for _ in range(r)]

    high = len(result)
    wide = len(result[0])
    cnt = 0

    for idx1 in range(high):
        for idx2 in range(wide):
            result[idx1][idx2] = nums[cnt]
            cnt += 1
    return result


if __name__ == '__main__':
    nums1 =[[1, 2], [3, 4]]
    print(matrixReshape(nums1, 1, 4))
    print(matrixReshape(nums1, 2, 4))