# -*- coding: utf-8 -*-

"""
Created on 2020-09-22 23:29
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def addBinary(a, b):
    if not a or not b : return a or b
    a, b, ans = a[::-1], b[::-1], []
    idx1 = idx2 = carry = 0
    while idx1 < len(a) or idx2 < len(b) or carry:
        num1 = int(a[idx1]) if idx1 < len(a) else 0
        num2 = int(b[idx2]) if idx2 < len(b) else 0
        carry, current = divmod(num1 + num2 + carry, 2)
        ans.append(str(current))
        idx1, idx2 = idx1+1, idx2+1
    return ''.join(ans[::-1])


if __name__ == '__main__':
    a = "11"
    b = "1"
    print(addBinary(a, b))  # 100
    a = "1010"
    b = "1011"
    print(addBinary(a, b))  # 10101
