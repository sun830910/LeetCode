# -*- coding: utf-8 -*-

"""
Created on 1/25/21 10:29 AM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.num_dic = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        if self.num_dic[carType] > 0:
            self.num_dic[carType] -= 1
            return True
        return False


if __name__ == '__main__':
    acts = ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
    targets = [[1, 1, 0], [1], [2], [3], [1]]
    result = []
    for idx in range(len(acts)):
        if acts[idx] == "ParkingSystem":
            assert len(targets[idx]) == 3
            test = ParkingSystem(targets[idx][0], targets[idx][1], targets[idx][2])
            result.append(None)
        elif acts[idx] == "addCar" and test is not None:
            result.append(test.addCar(targets[idx][0]))
    print(result)



