# -*- coding: utf-8 -*-

"""
Created on 1/6/21 4:11 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def isPrefixOfWord(sentence, searchWord):
    splited = sentence.strip().split()
    length = len(searchWord)
    for idx in range(len(splited)):
        if len(splited[idx]) >= length:
            if splited[idx][:length] == searchWord:
                return idx + 1
    return -1


if __name__ == '__main__':
    sentence = "i love eating burger"
    searchWord = "burg"
    print(isPrefixOfWord(sentence, searchWord))

    sentence = "this problem is an easy problem"
    searchWord = "pro"
    print(isPrefixOfWord(sentence, searchWord))

    sentence = "i am tired"
    searchWord = "you"
    print(isPrefixOfWord(sentence, searchWord))

    sentence = "i use triple pillow"
    searchWord = "pill"
    print(isPrefixOfWord(sentence, searchWord))