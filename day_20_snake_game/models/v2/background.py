from turtle import Screen
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from .board import Board
from enums import State


class Background:
    __score__: int = 0
    __high_score__: int = 0
    screen: Screen
    score_board: Board
    message_board: Board

    def __init__(self, screen: Screen):
        self.score_board = Board(0, SCREEN_HEIGHT/2 - 50)
        self.message_board = Board(0, 0)
        self.screen = screen

    def display_message_by_state(self, state: State):
        print(state)
        # Clear board before overwrite
        self.message_board.clear()
        self.score_board.clear()

        if state is State.GAME_OVER:
            self.__display_high_score()
            self.message_board.overwrite("GAME OVER!. PRESS SPACE TO START")
        elif state is State.PAUSE:
            self.__display_high_score()
            self.message_board.overwrite("PAUSE GAME. PRESS ESCAPE TO CONTINUE")
        elif state is State.WAIT:
            self.message_board.overwrite("PRESS SPACE TO START")
        else:
            self.score_board.overwrite(f"Score: {self.__score__}")()

        self.screen.update()

    def __display_high_score(self):
        self.score_board.overwrite(f"Score: {self.__score__} High Score: {self.__high_score__}")

    def update_score(self, score: int):
        self.__score__ = score
        self.__high_score__ = max(score, self.__high_score__)
