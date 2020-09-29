# -*- coding: utf-8 -*-

"""
Created on 2020-09-29 23:49
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def postorderTraversal(root):
    if not root:
        return []
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
        res.append(node.val)
    return res[::-1]

