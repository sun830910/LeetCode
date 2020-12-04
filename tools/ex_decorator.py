# -*- coding: utf-8 -*-

"""
Created on 12/4/20 9:02 AM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com

练习装饰器
"""

import logging


# 不带参数的装饰器
def say_hello(function):
    def wrapper():
        print("早上好")
        function()
        print("晚上好")

    return wrapper


@say_hello
def say_evening():
    print("中午好")


def decorator(function):
    def inside(l):
        try:
            function(l)
            print("排序结束")
        except:
            print("内部数据错误")

    return inside


@decorator
def show(lt):
    print("列表排序中")
    lt.sort()
    print(lt)


if __name__ == '__main__':
    # say_evening()
    lt = [3213, 21.3, True, '+', 3.21, '-', 3.21, 3.21, 3.21, 3.21, 3213123, 321, 3, 21, 3, 21, 3, 21, 321]
    show(lt)
