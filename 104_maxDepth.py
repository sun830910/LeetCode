# -*- coding: utf-8 -*-

"""
Created on 2020-09-27 23:31
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def maxDepth(root):
    if not root:
        return 0
    return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1