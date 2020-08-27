# -*- coding: utf-8 -*-

"""
Created on 2020-08-27 22:54
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

def masterMind(solution, guess):
    if len(solution) != len(guess):
        return
    answer0 = 0
    answer1 = 0
    solution_dict = dict()
    guess_dict = dict()
    for idx in range(len(solution)):
        if solution[idx] == guess[idx]:
            answer0 += 1
        else:
            if solution[idx] not in solution_dict:
                solution_dict.setdefault(solution[idx], 1)
            else:
                solution_dict[solution[idx]] += 1
            if guess[idx] not in guess_dict:
                guess_dict.setdefault(guess[idx], 1)
            else:
                guess_dict[guess[idx]] += 1

    for key in solution_dict.keys():
        if key in guess_dict:
            answer1 += min(guess_dict.get(key), solution_dict.get(key))

    return [answer0, answer1]

if __name__ == '__main__':
    solution = "RGBY"
    guess = "GGRR"
    print(masterMind(solution, guess))

