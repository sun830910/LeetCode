# -*- coding: utf-8 -*-

"""
Created on 11/20/20 5:10 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def reverseWords(s):
    splited = s.split(" ")
    result = []
    for word in splited:
        result.append(word[::-1])
    return " ".join(result)




if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    print(reverseWords(s))
