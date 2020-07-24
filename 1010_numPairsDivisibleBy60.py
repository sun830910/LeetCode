# -*- coding: utf-8 -*-

"""
Created on 2020-05-25 23:28
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def numPairsDivisibleBy60(time):
    # 超出时间限制
    res = 0
    for idx1 in range(len(time)):
        for idx2 in range(idx1+1,len(time)):
            if (time[idx1]+time[idx2])%60 ==0:
                res+=1
    return res

def numPairsDivisibleBy602(time):
    HashMap = {}
    cnt = 0
    for idx in range(len(time)):
        tmp = time[idx] % 60
        # 若res不在HashMap中则设为0
        HashMap.setdefault(tmp, 0)
        HashMap[tmp] += 1

    # 查看统计资料
    for idx in range(31):
        num1 = HashMap.get(idx)
        if idx in [0, 30]:
            if  num1 and num1>1:
                cnt += num1*(num1-1)//2
        else:
            num2 = HashMap.get(60-idx)
            if num1 and num2:
                cnt += num1*num2
    return cnt






if __name__ == '__main__':
    print(numPairsDivisibleBy602([30,20,150,100,40]))