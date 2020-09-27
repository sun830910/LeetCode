# -*- coding: utf-8 -*-

"""
Created on 2020-09-27 23:17
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def deleteDuplicates(head):
    node = head
    while node and node.next:
        if node.val == node.next.val:
            node.next = node.next.next
        else:
            node = node.next
    return head


