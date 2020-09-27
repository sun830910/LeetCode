# -*- coding: utf-8 -*-

"""
Created on 2020-09-27 23:09
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def lowestCommonAncestor(root, p, q):
    while root:
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            return root