# -*- coding: utf-8 -*-

"""
Created on 1/14/21 9:10 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def mergeTwoLists(l1, l2):
    result = ListNode(0)
    current = result
    while l1 and l2:
        if l1.val < l2.val:
            current.next, l1 = l1, l1.next
        else:
            current.next, l2 = l2, l2.next
        current = current.next
    current.next = l1 if l1 else l2
    return result.next