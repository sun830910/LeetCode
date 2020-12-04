# -*- coding: utf-8 -*-

"""
Created on 12/3/20 8:02 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""
import logging
import traceback
import random


# 自己创建的异常，继承自Exception
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class OuterError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr("超出范围啦")


def guess():
    answer = random.randint(0, 10)
    print("随机产生了1~10的答案")
    cnt = 1
    while True:
        print("----- 第 {} 局 -----".format(cnt))
        try:
            guess = int(input("请猜一个0~10的数: "))
            if guess == 24:
                raise MyError(guess)
            if guess > 10:
                raise OuterError(guess)
        except ValueError:
            print("输入的内容需为整数")
        except MyError as e:
            print("怎么会猜{}，触发了彩蛋".format(e.value))
        except OuterError as e:
            print("怎么会猜{},超出范围啦".format(e.value))

        else:
            if guess == answer:
                print("答对了")
                break
            elif guess < answer:
                print("猜大一点")
            else:
                print("猜小一点")
            cnt += 1
    print("Game Over")


if __name__ == '__main__':
    # raise_test()
    guess()
