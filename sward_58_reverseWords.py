# -*- coding: utf-8 -*-

"""
Created on 12/10/20 8:42 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def reverseWords(s):
    if not s:
        return ""
    splited = s.split(" ")
    while '' in splited:
        splited.remove('')
    return " ".join(splited[::-1])


if __name__ == '__main__':
    s = "the sky is blue"
    print(reverseWords(s))
    s = "  hello world!  "
    print(reverseWords(s))
    s = "a good   example"
    print(reverseWords(s))
