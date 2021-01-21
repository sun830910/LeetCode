# -*- coding: utf-8 -*-

"""
Created on 1/21/21 8:32 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def deleteNode(node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    node.val = node.next.val
    node.next = node.next.next