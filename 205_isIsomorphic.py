# -*- coding: utf-8 -*-

"""
Created on 12/27/20 10:52 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def isIsomorphic(s, t):
    if s == "" and t == "":
        return True
    if s == "" or t == "":
        return False
    record1 = dict()
    record2 = dict()
    for idx, vocab in enumerate(s):
        if vocab not in record1:
            record1[vocab] = [idx]
        else:
            record1[vocab].append(idx)
    for idx, vocab in enumerate(t):
        if vocab not in record2:
            record2[vocab] = [idx]
        else:
            record2[vocab].append(idx)
    for value in record1.values():
        if value not in record2.values():
            return False
    return True


if __name__ == '__main__':
    s = "egg"
    t = "add"
    print(isIsomorphic(s, t))  # T
    s = "foo"
    t = "bar"
    print(isIsomorphic(s, t))  # F
    s = "paper"
    t = "title"
    print(isIsomorphic(s, t))  # T
    s = "aba"
    t = "baa"
    print(isIsomorphic(s, t))  # F
