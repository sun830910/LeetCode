# -*- coding: utf-8 -*-

"""
Created on 2020-06-23 22:31
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def countCharacters(words, chars):
    char_dic = {}
    for char in chars:
        if char not in char_dic:
            char_dic[char] = 1
        else:
            char_dic[char] += 1

    result = 0
    for word in words:
        word_dic = {}
        for ch in word:
            if ch not in word_dic:
              word_dic[ch] = 1
            else:
                word_dic[ch] += 1
        for word_dic_idx in word_dic:
            if word_dic_idx not in char_dic:
                break
            if char_dic[word_dic_idx] < word_dic[word_dic_idx]:
                break
        else:
            result += len(word)
    return result


if __name__ == '__main__':
    print(countCharacters(words = ["cat","bt","hat","tree"], chars = "atach"))
