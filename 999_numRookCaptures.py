# -*- coding: utf-8 -*-

"""
Created on 12/7/20 4:35 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


def numRookCaptures(board):
    if not board or not board[0]:
        return
    def find_R(board):
        for row_idx in range(len(board)):
            if 'R' in board[row_idx]:
                col_idx = board[row_idx].index('R')
                return [row_idx, col_idx]

    def transfer(arr):
        result = 0
        tmp = ""
        for vocab in arr:
            if vocab != '.':
                tmp += vocab
        if 'Rp' in tmp:
            result += 1
        if 'pR' in tmp:
            result += 1
        return result

    position = find_R(board)
    row_idx = position[0]
    col_idx = position[1]
    row_list = board[row_idx]
    column_list = [board[_][col_idx] for _ in range(len(board))]
    row_result = transfer(row_list)
    column_result = transfer(column_list)
    return row_result + column_result


if __name__ == '__main__':
    board = [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
             [".", ".", ".", "R", ".", ".", ".", "p"], [".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]
    print(numRookCaptures(board))

    board = [[".", ".", ".", ".", ".", ".", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."],
             [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "B", "R", "B", "p", ".", "."],
             [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]

    print(numRookCaptures(board))

    board = [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
             [".", ".", ".", "p", ".", ".", ".", "."], ["p", "p", ".", "R", ".", "p", "B", "."],
             [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "B", ".", ".", ".", "."],
             [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]

    print(numRookCaptures(board))
