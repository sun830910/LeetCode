# -*- coding: utf-8 -*-

"""
Created on 1/12/21 8:47 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def replaceSpace(s):
    result = ""
    for idx in s:
        if idx != " ":
            result += idx
        else:
            result += "%20"
    return result


if __name__ == '__main__':
    s = "We are happy."
    print(replaceSpace(s))
    s = ""
    print(replaceSpace(s))
