# -*- coding: utf-8 -*-

"""
Created on 1/5/21 4:08 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def reorderSpaces(text):
    space_cnt = text.count(' ')
    words = text.strip().split()
    if len(words) == 1:
        return words[0] + ' ' * space_cnt
    every, other = divmod(space_cnt, len(words) - 1)
    return (' ' * every).join(words) + (' ' * other)


if __name__ == '__main__':
    text = "  this   is  a sentence "
    print(reorderSpaces(text))  # "this   is   a   sentence"
    text = " practice   makes   perfect"
    print(reorderSpaces(text))
    text = "hello   world"
    print(reorderSpaces(text))
    text = "  walks  udp package   into  bar a"
    print(reorderSpaces(text))
    text = "a"
    print(reorderSpaces(text))
