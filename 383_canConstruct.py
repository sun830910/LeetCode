# -*- coding: utf-8 -*-

"""
Created on 12/20/20 10:45 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def canConstruct(ransomNote, magazine):
    if ransomNote == magazine:
        return True
    if not magazine:
        return False
    record1 = dict()
    record2 = dict()
    for vocab in ransomNote:
        if vocab not in record1:
            record1.setdefault(vocab, 1)
        else:
            record1[vocab] += 1
    for vocab in magazine:
        if vocab not in record2:
            record2.setdefault(vocab, 1)
        else:
            record2[vocab] += 1
    for key in record1.keys():
        if key not in record2:
            return False
        if record1[key] > record2[key]:
            return False
    return True

if __name__ == '__main__':
    print(canConstruct("a", "b"))
    print(canConstruct("aa", "ab"))
    print(canConstruct("aa", "aab"))
    print(canConstruct("", ""))
    print(canConstruct("", "a"))
    print(canConstruct("", " "))