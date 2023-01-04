import numpy as np

BOARD_LENGTH = 5

DIRECTION_OPTIONS = (
    np.array((1, 0, 0)),
    np.array((-1, 0, 0)),
    np.array((0, 1, 0)),
    np.array((0, -1, 0)),
    np.array((0, 0, 1)),
    np.array((0, 0, -1)),
)

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

ROTATION_OPTIONS.append(ROTATION_OPTIONS[0] * -1)
ROTATION_OPTIONS.append(ROTATION_OPTIONS[1] * -1)
