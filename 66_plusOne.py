# -*- coding: utf-8 -*-

"""
Created on 2020-05-31 18:33
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def plusOne(digits):
    tmp = ''
    for idx in range(len(digits)):
        tmp += str(digits[idx])
    tmp = int(tmp)+1
    result = []
    for tmp_idx in str(tmp):
        result.append(int(tmp_idx))
    return result

def plusOne2(digits):
    nums = int(''.join(str(idx) for idx in digits))+1
    return [int(num) for num in str(nums)]
if __name__ == '__main__':
    print(plusOne([1,2,3]))
    print(plusOne2([1, 2, 3]))