# -*- coding: utf-8 -*-

"""
Created on 1/24/21 12:41 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def kthToLast(head, k):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr[-k]
