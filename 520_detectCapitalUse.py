# -*- coding: utf-8 -*-

"""
Created on 11/20/20 4:29 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

# 73%
def detectCapitalUse(word):
    if not word:
        return
    big = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    small = set("abcdefghijklmnopqrstuvwxyz")
    otherBig = False
    otherSmall = False
    for idx, vocab in enumerate(word):
        if vocab in small:
            otherSmall = True
        if otherSmall and vocab in big:
            return False
        if vocab in big and idx != 0:
            otherBig = True
        if otherBig and vocab in small:
            return False
    return True


if __name__ == '__main__':
    print(detectCapitalUse("USA"))
    print(detectCapitalUse("leetcode"))
    print(detectCapitalUse("Google"))
    print(detectCapitalUse("FlaG"))
    print(detectCapitalUse("sS"))
    print(detectCapitalUse("sSs"))
