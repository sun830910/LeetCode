# -*- coding: utf-8 -*-

"""
Created on 11/30/20 2:25 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def hasGroupsSizeX(deck):
    # 求最大公因数
    def calc(x, y) -> int:
        if x % y == 0:
            return y
        else:
            return calc(y, x % y)

    if not deck:
        return False
    record = dict()

    for card in deck:
        if card not in record:
            record.setdefault(card, 1)
        else:
            record[card] += 1
    base = record[deck[0]]
    for key, val in record.items():
        tmp1 = max(base, val)
        tmp2 = min(base, val)
        base = calc(tmp1, tmp2)
        if base < 2:
            return False
    return True


if __name__ == '__main__':
    deck = [1, 2, 3, 4, 4, 3, 2, 1]
    print(hasGroupsSizeX(deck))  # T
    deck = [1, 1, 1, 2, 2, 2, 3, 3]
    print(hasGroupsSizeX(deck))  # F
    deck = [1]
    print(hasGroupsSizeX(deck))  # F
    deck = [1, 1]
    print(hasGroupsSizeX(deck))  # T
    deck = [1, 1, 2, 2, 2, 2]
    print(hasGroupsSizeX(deck))  # T
    deck = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2]
    print(hasGroupsSizeX(deck))  # T
