# -*- coding: utf-8 -*-

"""
Created on 2020-11-02 19:57
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def plusOne(digits):
    digits[-1] += 1
    flag = 0
    idx = len(digits)-1
    while idx >= 0:
        if digits[idx] + flag >= 10:
            digits[idx] = (digits[idx] + flag) % 10
            flag = 1
            idx -= 1
        else:
            digits[idx] = digits[idx] + flag
            flag = 0
            idx -= 1
    if flag:
        digits.insert(0, 1)

    return digits



if __name__ == '__main__':
    nums = [1, 2, 3]
    print(plusOne(nums))

    nums = [4, 3, 2, 1]
    print(plusOne(nums))

    nums = [9]
    print(plusOne(nums))

    nums = [1, 3, 9]
    print(plusOne(nums))

    nums = [9, 9]
    print(plusOne(nums))

    nums = [1, 9, 9]
    print(plusOne(nums))

    nums = [0]
    print(plusOne(nums))
