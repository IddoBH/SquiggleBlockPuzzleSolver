import numpy as np

import constants
from helper_functions import place_block

GAME_BOARD = np.zeros((constants.BOARD_LENGTH, constants.BOARD_LENGTH, constants.BOARD_LENGTH))


def solve(board):
    solution = []
    solve_reccursive(solution, board)


def solve_reccursive(current_solution, board):
    if board.sum() == 125:
        return True

    for i in range(constants.BOARD_LENGTH):
        for j in range(constants.BOARD_LENGTH):
            for k in range(constants.BOARD_LENGTH):
                if board[i][j][k] == 0:
                    for direction in constants.DIRECTION_OPTIONS:
                        for rotation in constants.ROTATION_OPTIONS:
                            if place_block(board, (i, j, k), direction, rotation):
                                if solve_reccursive(current_solution, board):
                                    current_solution.append(((i, j, k), direction, rotation))
                                    return True
    return False

if __name__ == '__main__':
    solution = solve(GAME_BOARD)
    print(solution, GAME_BOARD)
