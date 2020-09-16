# -*- coding: utf-8 -*-

"""
Created on 2020-09-16 16:47
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def longestCommonPrefix(strs):
    result = ""
    for tmp in zip(*strs):
        tmp_set = set(tmp)
        if len(tmp_set) == 1:
            result += tmp[0]
        else:
            break  # 只要一个索引超过两个数就打断
    return result


if __name__ == '__main__':
    test1 = ["flower","flow","flight"]
    print(longestCommonPrefix(test1))

    test2 = ["dog","racecar","car"]
    print(longestCommonPrefix(test2))
