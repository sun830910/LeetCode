# -*- coding: utf-8 -*-

"""
Created on 1/29/21 3:43 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def isSymmetric(root):
    if not root:
        return True

    def helper(left_node, right_node):
        if not (left_node or right_node):  # 若left_node和right_node相同，且都为空
            return True
        if not (left_node and right_node):  # 若left_node和right_node有一个为空
            return False
        if left_node.val != right_node.val:
            return False
        return helper(left_node.left, right_node.right) and helper(left_node.right, right_node.left)

    return helper(root.left, root.right)