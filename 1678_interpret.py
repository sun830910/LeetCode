# -*- coding: utf-8 -*-

"""
Created on 1/23/21 1:30 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def interpret(command):
    result = ""
    if not command:
        return result
    idx = 0
    while idx < len(command):
        if command[idx] == '(':
            if command[idx + 1] == ')':
                result += 'o'
                idx += 2
            else:
                result += 'al'
                idx += 4
        else:
            result += 'G'
            idx += 1
    return result


if __name__ == '__main__':
    command = "G()(al)"
    print(interpret(command))
    command = "G()()()()(al)"
    print(interpret(command))
    command = "(al)G(al)()()G"
    print(interpret(command))
