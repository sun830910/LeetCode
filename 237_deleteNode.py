# -*- coding: utf-8 -*-

"""
Created on 1/23/21 10:16 AM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def deleteNode(node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    node.val = node.next.val
    node.next = node.next.next
