# -*- coding: utf-8 -*-

"""
Created on 12/31/20 3:31 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

import re

# 超出时间限制
# def isSubsequence(s, t):
#     list_s = list(s)
#     pattern = '.*'.join(list_s)
#     pattern = '.*' + pattern + '.*'
#     if re.search(pattern, t):
#         return True
#     return False


def isSubsequence(s, t):
    s_idx = 0
    t_idx = 0
    while s_idx < len(s) and t_idx < len(t):
        if s[s_idx] == t[t_idx]:
            s_idx += 1
            t_idx += 1
        else:
            t_idx += 1
    if s_idx == len(s):
        return True
    return False



if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    print(isSubsequence(s, t))

    s = "axc"
    t = "ahbgdc"
    print(isSubsequence(s, t))

    s = "rjufvjafbxnbgriwgokdgqdqewn"
    t = "mjmqqjrmzkvhxlyruonekhhofpzzslupzojfuoztvzmmqvmlhgqxehojfowtrinbatjujaxekbcydldglkbxsqbbnrkhfdnpfbuaktupfftiljwpgglkjqunvithzlzpgikixqeuimmtbiskemplcvljqgvlzvnqxgedxqnznddkiujwhdefziydtquoudzxstpjjitmiimbjfgfjikkjycwgnpdxpeppsturjwkgnifinccvqzwlbmgpdaodzptyrjjkbqmgdrftfbwgimsmjpknuqtijrsnwvtytqqvookinzmkkkrkgwafohflvuedssukjgipgmypakhlckvizmqvycvbxhlljzejcaijqnfgobuhuiahtmxfzoplmmjfxtggwwxliplntkfuxjcnzcqsaagahbbneugiocexcfpszzomumfqpaiydssmihdoewahoswhlnpctjmkyufsvjlrflfiktndubnymenlmpyrhjxfdcq"
    print(isSubsequence(s, t))