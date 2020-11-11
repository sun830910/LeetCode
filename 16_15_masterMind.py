# -*- coding: utf-8 -*-

"""
Created on 2020-11-11 15:37
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def masterMind(solution, guess):
    if not solution or not guess or len(solution) != len(guess):
        return [0, 0]
    correct_cnt = 0
    record_solution = dict()
    record_guess = dict()
    for idx in range(len(solution)):
        if solution[idx] == guess[idx]:
            correct_cnt += 1
        else:
            if solution[idx] not in record_solution:
                record_solution.setdefault(solution[idx], 1)
            else:
                record_solution[solution[idx]] += 1
            if guess[idx] not in record_guess:
                record_guess.setdefault(guess[idx], 1)
            else:
                record_guess[guess[idx]] += 1
    error_cnt = 0
    for key in record_solution:
        if key in record_guess:
            error_cnt += min(record_solution.get(key), record_guess.get(key))
    return [correct_cnt, error_cnt]



if __name__ == '__main__':
    solution = "RGBY"
    guess = "GGRR"
    print(masterMind(solution, guess))
