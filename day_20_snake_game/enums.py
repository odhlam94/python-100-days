from enum import Enum


class Direction(Enum):
    UP_DEGREE = 90
    DOWN_DEGREE = 270
    LEFT_DEGREE = 180
    RIGHT_DEGREE = 0


class State(Enum):
    WAIT = 0
    PLAYING = 1
    PAUSE = 2
    GAME_OVER = 3

