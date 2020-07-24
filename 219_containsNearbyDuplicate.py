# -*- coding: utf-8 -*-

"""
Created on 2020-06-22 23:24
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def containsNearbyDuplicate(nums, k):
    done = {}
    for idx in range(len(nums)):
        if nums[idx] not in done:
            done[nums[idx]] = idx
        else:
            if idx - done.get(nums[idx]) <= k:
                return True
            else:
                done[nums[idx]] = idx
    return False

if __name__ == '__main__':
    print(containsNearbyDuplicate([1,2,3,1], 3))
    print(containsNearbyDuplicate([1,0,1,1],1))
    print(containsNearbyDuplicate([1,2,3,1,2,3],2))