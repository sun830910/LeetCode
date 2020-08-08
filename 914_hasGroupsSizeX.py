# -*- coding: utf-8 -*-

"""
Created on 2020-08-08 12:05
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def hasGroupsSizeX(deck):
    cnt_dict = dict()
    for deck_idx in deck:
        if deck_idx not in cnt_dict:
            cnt_dict.setdefault(deck_idx, 1)
        else:
            cnt_dict[deck_idx] += 1

    cnt_dict_list = list(cnt_dict.values())

    if min(cnt_dict_list) < 2:
        return False
    # 找最大公约数，查找范围是2~cnt_dict_list中最小的数，只要有整除项，代表在所有的数中有2以上的最大公因数
    for X in range(2, min(cnt_dict_list) + 1):
        success = 1
        for num in cnt_dict_list:
            if num % X != 0:
                success = 0
        if success == 1:
            return True
    return False



if __name__ == '__main__':

    test1 = [1,2,3,4,4,3,2,1]
    print(hasGroupsSizeX(test1)) # True
    test2 = [1,1,1,2,2,2,3,3]
    print(hasGroupsSizeX(test2)) # False
    test3 = [1]
    print(hasGroupsSizeX(test3)) # False
    test4 = [1, 1]
    print(hasGroupsSizeX(test4)) # True
    test5 = [1,1,2,2,2,2]
    print(hasGroupsSizeX(test5)) # True
    test6 = [1,1,1,1,1,0,0,0]
    print(hasGroupsSizeX(test6)) # False

