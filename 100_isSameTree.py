# -*- coding: utf-8 -*-

"""
Created on 12/26/20 4:51 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
