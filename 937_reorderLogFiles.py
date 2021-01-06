# -*- coding: utf-8 -*-

"""
Created on 1/6/21 3:39 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def reorderLogFiles(logs):
    digitLog = []
    letterLog = []
    for s in logs:
        if s.split(" ")[1][0].isdigit():
            digitLog.append(s)
        if s.split(" ")[1][0].isalpha():
            letterLog.append(s)
    letterLog = sorted(letterLog, key=lambda s: s.split(" ")[0])
    letterLog = sorted(letterLog, key=lambda s: " ".join(s.split(" ")[1:]))
    result = letterLog + digitLog
    return result


if __name__ == '__main__':
    logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
    print(reorderLogFiles(logs))
    logs = ["j je", "b fjt", "7 zbr", "m le", "o 33"]
    print(reorderLogFiles(logs))  # ["b fjt","j je","m le","7 zbr","o 33"]
