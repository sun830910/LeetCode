# -*- coding: utf-8 -*-

"""
Created on 1/8/21 2:50 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


# def minArray(numbers):
#     return min(numbers)


def minArray(numbers):
    left = 0
    right = len(numbers) - 1
    while left < right:
        mid = (left + right) // 2
        if numbers[mid] > numbers[right]:  # mid为左侧有序数组中的点，往右查旋转点
            left = mid + 1
        elif numbers[mid] < numbers[right]:  # mid为右侧有序数组中的点，往左查旋转点
            right = mid
        else:  # mid与right值相同时，缩右侧
            right -= 1
    return numbers[left]


if __name__ == '__main__':
    numbers = [3, 4, 5, 1, 2]
    print(minArray(numbers))
    numbers = [2, 2, 2, 0, 1]
    print(minArray(numbers))
    numbers = [2, 1, 2, 2]
    print(minArray(numbers))
