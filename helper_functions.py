import numpy as np

import constants


def generate_sequence(direction, rotation):
    return direction, direction, direction @ rotation, direction


def place_block(board, position, direction, rotation):
    temp_board = np.zeros((constants.BOARD_LENGTH, constants.BOARD_LENGTH, constants.BOARD_LENGTH))
    temp_pos = np.asarray(position)
    temp_board[temp_pos[0]][temp_pos[1]][temp_pos[2]] = 1
    sequence = generate_sequence(direction, rotation)
    for step in sequence:
        temp_pos += step
        if any((i < 0 or i >= 5 for i in temp_pos)) or board[temp_pos[0]][temp_pos[1]][temp_pos[2]]:
            return False
        temp_board[temp_pos[0]][temp_pos[1]][temp_pos[2]] = 1
    board += temp_board
    return True

def remove_block(board, position, direction, rotation):
    temp_pos = np.asarray(position)
    board[temp_pos[0]][temp_pos[1]][temp_pos[2]] = 0
    sequence = generate_sequence(direction, rotation)
    for step in sequence:
        temp_pos += step
        board[temp_pos[0]][temp_pos[1]][temp_pos[2]] = 0


