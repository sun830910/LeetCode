# -*- coding: utf-8 -*-

"""
Created on 11/26/20 9:48 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


# 11 %
# def singleNumber(nums):
#     record = set()
#     result = []
#     for num in nums:
#         if num not in record and num not in result:
#             result.append(num)
#         else:
#             result.remove(num)
#             record.add(num)
#     return result[0]

# 数组中有且只有一个唯一数，其余数都是2次。都是2次，都是2次！！
def singleNumber(nums):
    sum1 = sum(nums)
    sum2 = sum(set(nums))
    return 2 * sum2 - sum1


if __name__ == '__main__':
    nums = [2, 2, 1]
    print(singleNumber(nums))
