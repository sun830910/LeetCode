# -*- coding: utf-8 -*-

"""
Created on 2020-09-16 17:02
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def isValid(s):
    stack = []
    for idx in s:
        if idx in ['(', '[', '{']:
            stack.append(idx)
        elif idx == ')' and len(stack) != 0 and stack[-1] == '(':
            stack.pop()
        elif idx == ']' and len(stack) != 0 and stack[-1] == '[':
            stack.pop()
        elif idx == '}' and len(stack) != 0 and stack[-1] == '{':
            stack.pop()
        else:
            return False
    if len(stack) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    test1 = "()"
    print(isValid(test1))  # t
    test2 = "()[]{}"
    print(isValid(test2))  # t
    test3 = "(]"
    print(isValid(test3))  # f
    test4 = "([)]"
    print(isValid(test4))  # f
    test5 = "{[]}"
    print(isValid(test5))  # t
    test6 = "["
    print(isValid(test6))  # f
    test7 = "]"
    print(isValid(test7))  # f
