import numpy as np

BOARD_LENGTH = 5

DIRECTION_OPTIONS = {
    'X': np.array((1, 0, 0)),
    '-X': np.array((-1, 0, 0)),
    'Y': np.array((0, 1, 0)),
    '-Y': np.array((0, -1, 0)),
    'Z': np.array((0, 0, 1)),
    '-Z': np.array((0, 0, -1)),
}

ROTATION_OPTIONS = [
    np.array((
        (0, 1, 0),
        (0, 0, 1),
        (1, 0, 0)
    )),
    np.array((
        (0, 0, 1),
        (1, 0, 0),
        (0, 1, 0)
    ))
]

ROTATION_OPTIONS.append(ROTATION_OPTIONS[0]*-1)
ROTATION_OPTIONS.append(ROTATION_OPTIONS[1]*-1)
