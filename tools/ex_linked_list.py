# -*- coding: utf-8 -*-

"""
Created on 11/25/20 4:22 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


class Node(object):
    # 结点初始化函数, p 即模拟所存放的下一个结点的地址
    # 为了方便传参, 设置 p 的默认值为 0
    def __init__(self, data, p=0):
        self.data = data
        self.next = p


class LinkedList(object):
    def __init__(self):
        self.head = None

    # 链表初始化函数, 方法类似于尾插
    def initList(self, data):
        # 创建头节点
        self.head = Node(data[0])
        p = self.head
        # 遍历数据创建结点建立链表
        for idx in data[1:]:
            node = Node(idx)
            p.next = node
            p = p.next

    # 链表判空
    def isEmpty(self):
        if self.head.next == 0:
            print("Empty List!")
            return 1
        else:
            return 0

    # 取链表长度
    def getLength(self):
        if self.isEmpty():
            return 0

        p = self.head
        len = 0
        while p:
            len += 1
            p = p.next
        return len

    # 遍历链表
    def traveList(self):
        if self.isEmpty():
            return 0
        p = self.head
        while p:
            print(p.data)
            p = p.next

    # 链表插入数据函数
    def insertElem(self, key, index):
        if self.isEmpty():
            return 0
        if index < 0 or index > self.getLength() - 1:
            return 0

        p = self.head
        i = 0
        while i <= index:
            pre = p
            p = p.next
            i += 1

        # 遍历找到索引值为 index 的结点后, 在其后面插入结点
        node = Node(key)
        pre.next = node
        node.next = p

    # 链表删除数据函数
    def deleteElem(self, index):
        if self.isEmpty():
            return 0
        if index < 0 or index > self.getLength() - 1:
            return 0

        i = 0
        p = self.head
        # 遍历找到索引值为 index 的结点
        while p.next:
            pre = p
            p = p.next
            i += 1
            if i == index:
                pre.next = p.next
                p = None
                return 1

        # p的下一个结点为空说明到了最后一个结点, 删除之即可
        pre.next = None


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    l = LinkedList()
    l.initList(data)
    l.traveList()

    print("=" * 30)

    # 插入结点到索引值为3之后, 值为666
    l.insertElem(666, 3)
    l.traveList()

    print("=" * 30)

    l.deleteElem(4)
    l.traveList()