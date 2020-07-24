# -*- coding: utf-8 -*-

"""
Created on 2020-06-22 22:40
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def majorityElement(nums):
    dic = {}
    for num in nums:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1
    return max(dic.keys() , key=lambda x: dic[x])

def majorityElement2(nums):
    if nums is None or len(nums) < 2:
        return
    cnt = 0
    major = 0
    for num in nums:
        if cnt == 0:
            major = num
        if num == major:
            cnt += 1
        else:
            cnt -= 1
    return major

def majorityElementsTest(nums):
    if nums is None or len(nums)<2:
        return
    major = 0
    cnt = 0
    for num in nums:
        if cnt == 0:
            major = num
        if major == num:
            cnt += 1
        else:
            cnt -= 1
    return major

if __name__ == '__main__':
    test1 = [3, 2, 3]
    test2 = [2, 2, 1, 1, 1, 2, 2]
    print(majorityElement(test1))
    print(majorityElement(test2))
    print('=========================')
    print(majorityElement2(test1))
    print(majorityElement2(test2))
    print('=========================')
    print(majorityElementsTest(test1))
    print(majorityElementsTest(test2))