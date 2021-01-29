# -*- coding: utf-8 -*-

"""
Created on 1/29/21 4:11 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def maxDepth(root):
    if not root:
        return 0
    left_maxDepth = self.maxDepth(root.left)
    right_maxDepth = self.maxDepth(root.right)
    return max(left_maxDepth, right_maxDepth) + 1
