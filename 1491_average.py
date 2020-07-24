# -*- coding: utf-8 -*-

"""
Created on 2020-07-15 23:09
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

def mergeSort(nums):
    if len(nums) < 2:
        return nums
    mid_idx = len(nums)//2
    left, right = nums[:mid_idx], nums[mid_idx:]
    return merge(mergeSort(left),mergeSort(right))

def average(salary):
    sort_salary = mergeSort(salary)
    sort_salary.pop()
    sort_salary.pop(0)
    total_salary_num = len(sort_salary)
    total_salary = 0
    while sort_salary:
        total_salary += sort_salary.pop(0)

    return total_salary/total_salary_num

if __name__ == '__main__':
    test = [8000,9000,2000,3000,6000,1000]
    print(average(test))

