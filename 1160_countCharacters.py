# -*- coding: utf-8 -*-

"""
Created on 11/27/20 4:13 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def countCharacters(words, chars):
    def check(record, current):
        for key in current:
            if key not in record:
                return False
            if record.get(key) < current.get(key):
                return False
        return True

    record = dict()
    result = 0
    for char in chars:
        if char not in record:
            record.setdefault(char, 1)
        else:
            record[char] += 1
    for word in words:
        current = dict()
        for ch in word:
            if ch not in current:
                current.setdefault(ch, 1)
            else:
                current[ch] += 1
        if check(record, current):
            result += len(word)
    return result


if __name__ == '__main__':
    words = ["cat", "bt", "hat", "tree"]
    chars = "atach"
    print(countCharacters(words, chars))
