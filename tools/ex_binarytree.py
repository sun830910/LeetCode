# -*- coding: utf-8 -*-

"""
Created on 12/31/20 2:04 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


class TreeNode():
    """
    定义树节点
    data：存储的数据
    left：左子树
    right：右子树
    """

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinTree():
    """
    创建二叉树
    """

    def __init__(self):
        self.root = None  # 初始化根节点为None
        self.ls = []  # 定义列表用于存储节点地址

    def add(self, data):
        """
        定义add方法向树结构中添加元素
        :param data:
        :return:
        """
        node = TreeNode(data)  # 实例化树节点
        if self.root == None:  # 若根节点为None，添加根节点，并将根节点地址值添加到self.ls中
            self.root = node
            self.ls.append(self.root)
        else:
            rootNode = self.ls[0]  # 将第一个元素设为根节点
            if rootNode.left == None:  # 若根节点的左子树为None，添加左节点，并将其地址添加到self.ls中
                rootNode.left = node
                self.ls.append(rootNode.left)
            elif rootNode.right == None:  # 若根节点的右子树为None，添加右节点，并将其地址添加到self.ls中
                rootNode.right = node
                self.ls.append(rootNode.right)
                self.ls.pop(0)  # 弹出self.ls第一个位置处的元素


if __name__ == '__main__':
    arr = [idx for idx in range(11)]
    tree = BinTree()
    for idx in arr:
        tree.add(idx)
    print(tree)
