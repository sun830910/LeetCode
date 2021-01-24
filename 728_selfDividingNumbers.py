# -*- coding: utf-8 -*-

"""
Created on 1/24/21 12:26 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def selfDividingNumbers(left, right):
    result = []
    if not left or not right:
        return result

    def check(num):
        divided = num
        while divided:
            current = divided % 10
            if current == 0 or num % current != 0:
                return False
            divided = divided // 10
        return True

    for idx in range(left, right + 1):
        if check(idx):
            result.append(idx)
    return result


if __name__ == '__main__':
    left = 1
    right = 22
    print(selfDividingNumbers(left, right))
