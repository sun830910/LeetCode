# -*- coding: utf-8 -*-

"""
Created on 1/13/21 5:03 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def reversePrint(head):
    result = []
    if not head:
        return result
    result.append(head.val)
    while head.next:
        head = head.next
        result.append(head.val)
    return result[::-1]
