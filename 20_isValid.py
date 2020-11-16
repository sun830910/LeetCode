# -*- coding: utf-8 -*-

"""
Created on 2020-11-16 16:04
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def isValid(s):
    result = []
    for word in s:
        if len(result) < 1:
            result.append(word)
            continue
        if word == ")" and result[-1] == "(":
            result.pop()
        elif word == "}" and result[-1] == "{":
            result.pop()
        elif word == "]" and result[-1] == "[":
            result.pop()
        else:
            result.append(word)

    if len(result) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    s = "()"
    print(isValid(s))
    s = "()[]{}"
    print(isValid(s))
    s = "(]"
    print(isValid(s))
    s = "([)]"
    print(isValid(s))
    s = "{[]}"
    print(isValid(s))
    s = "]"
    print(isValid(s))
    s = "({[)"
    print(isValid(s))