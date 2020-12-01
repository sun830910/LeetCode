# -*- coding: utf-8 -*-

"""
Created on 12/1/20 3:56 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def commonChars(A):
    if not A:
        return
    result = []
    record_word = dict()
    for vocab in A[0]:
        if vocab not in record_word:
            record_word.setdefault(vocab, 1)
        else:
            record_word[vocab] += 1
    for idx in range(1, len(A)):
        record_current = dict()
        for vocab in A[idx]:
            if vocab not in record_current:
                record_current.setdefault(vocab, 1)
            else:
                record_current[vocab] += 1
        if len(record_word.keys()) == 0:
            return result
        remove_list = []
        for key, cnt in record_word.items():
            if key not in record_current:
                remove_list.append(key)
            else:
                record_word[key] = min(cnt, record_current.get(key))
        for remove in remove_list:
            record_word.pop(remove)
    for key, cnt in record_word.items():
        for _ in range(cnt):
            result.append(key)

    return result


if __name__ == '__main__':
    A = ["bella", "label", "roller"]
    print(commonChars(A))
    A = ["cool", "lock", "cook"]
    print(commonChars(A))
