import numpy as np

GAME_BOARD = np.zeros((5, 5, 5))


def place_block(position, direction, rotation):
    temp_pos = np.asarray(position)
    toggle_place(temp_pos)
    sequence = ((0,0,1),(0,0,1),(0,1,0),(0,0,1))
    for step in sequence:
        temp_pos += step
        toggle_place(temp_pos)


def toggle_place(coordinates):
    GAME_BOARD[coordinates[0]][coordinates[1]][coordinates[2]] = 1 - GAME_BOARD[coordinates[0]][coordinates[1]][coordinates[2]]


if __name__ == '__main__':
    place_block((0, 0, 0), 0, 0)
    print(GAME_BOARD)
