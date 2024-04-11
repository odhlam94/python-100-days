from constants import SCREEN_HEIGHT
from .board import Board
from enums import State
from .food import Food
from .shared import screen
from .snake import Snake


class Context:
    __score: int = 0
    __high_score: int = 0
    __score_board: Board
    __message_board: Board
    state: State
    snake: Snake
    food: Food

    def __init__(self):
        self.__score_board = Board(0, SCREEN_HEIGHT / 2 - 50)
        self.__message_board = Board(0, 0)
        self.snake = Snake()
        self.food = Food()

    def __appearance_by_state(self):
        # Clear board before overwrite
        self.__message_board.clear()
        self.__score_board.clear()

        self.show_hide_component(is_show=False)

        if self.state is State.GAME_OVER:
            self.__display_high_score()
            self.__message_board.overwrite("GAME OVER!. PRESS SPACE TO START")
        elif self.state is State.PAUSE:
            self.__display_high_score()
            self.__message_board.overwrite("PAUSE GAME. PRESS ESCAPE TO CONTINUE")
        elif self.state is State.WAIT:
            self.__message_board.overwrite("PRESS SPACE TO START")
        else:
            self.__score_board.overwrite(f"Score: {self.__score}")
            self.show_hide_component(is_show=True)

        screen.update()

    def show_hide_component(self, is_show):
        self.food.showturtle() if is_show else self.food.hideturtle()
        for seg in self.snake.segments:
            seg.showturtle() if is_show else seg.hideturtle()

    def __display_high_score(self):
        self.__score_board.overwrite(f"Score: {self.__score} High Score: {self.__high_score}")

    def increase_score(self):
        self.set_score(score=self.__score + 1)

    def set_score(self, score: int):
        self.__score = score
        self.__high_score = max(self.__score, self.__high_score)
        self.__appearance_by_state()

    def set_state(self, state: State):
        self.state = state
        self.__appearance_by_state()
