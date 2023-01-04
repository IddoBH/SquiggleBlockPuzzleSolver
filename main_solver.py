import numpy as np

import constants
from helper_functions import place_block, remove_block

GAME_BOARD = np.zeros((constants.BOARD_LENGTH, constants.BOARD_LENGTH, constants.BOARD_LENGTH))


def solve(board):
    solution = []
    result = solve_reccursive(solution, board)
    return solution if result else False


FAILING_BOARDS = []


def solve_reccursive(current_solution, board, shift=1):
    if board.sum() == 125:
        return True

    for fb in FAILING_BOARDS:
        if (fb == board).all():
            return False

    for i in range(constants.BOARD_LENGTH):
        for j in range(constants.BOARD_LENGTH):
            for k in range(constants.BOARD_LENGTH):
                if board[i][j][k] == 0:
                    for direction in constants.DIRECTION_OPTIONS:
                        for rot_idx in range(len(constants.ROTATION_OPTIONS)):
                            if place_block(board, (i, j, k), direction, constants.ROTATION_OPTIONS[(rot_idx + shift) % 4]):
                                print(board.sum() / 5)
                                if solve_reccursive(current_solution, board, (shift + 1) % 4):
                                    current_solution.append(((i, j, k), direction, constants.ROTATION_OPTIONS[(rot_idx + shift) % 4]))
                                    return True
                                else:
                                    remove_block(board, (i, j, k), direction, constants.ROTATION_OPTIONS[(rot_idx + shift) % 4])
    for fb in FAILING_BOARDS:
        if (fb == board).all():
            return False

    FAILING_BOARDS.append(board.copy())
    return False


if __name__ == '__main__':
    solution = solve(GAME_BOARD)
    print(solution, GAME_BOARD)
