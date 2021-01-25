# -*- coding: utf-8 -*-

"""
Created on 1/25/21 10:24 AM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def defangIPaddr(address):
    result = ""
    for idx in range(len(address)):
        if address[idx] == ".":
            result += "[.]"
        else:
            result += address[idx]
    return result


if __name__ == '__main__':
    address = "1.1.1.1"
    print(defangIPaddr(address))
    address = "255.100.50.0"
    print(defangIPaddr(address))
