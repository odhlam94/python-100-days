from constants import MOVE_DISTANCE
from enums import State
from .context import Context
from .food import Food
from time import sleep
from .shared import screen


class GamePlay:
    context: Context

    def __init__(self):
        self.context = Context()

        # Config keydown to start or pause game
        screen.onkey(key="space", fun=self.play)
        screen.onkey(key="Escape", fun=self.pause_continue)

    def start(self):
        self.context.snake.refresh()
        self.context.set_state(State.WAIT)
        screen.exitonclick()

    def play(self):
        self.context.set_state(State.PLAYING)
        while self.context.state is State.PLAYING:
            # Game over if snake header touched any snack's segment
            if self.context.snake.move() is State.GAME_OVER:
                self.context.set_state(State.GAME_OVER)
            # Snack header touched the food
            self.__handle_touched_food()
            # Delay 0.1 second before next time moving
            sleep(0.1)

    def pause_continue(self):
        state = (State.PLAYING if self.context.state is State.PAUSE else State.PAUSE)
        self.context.set_state(state)
        if state == State.PLAYING:
            self.play()

    def __handle_touched_food(self):
        if self.context.snake.head.distance(self.context.food) < MOVE_DISTANCE:
            self.context.snake.extend(self.context.food)
            self.context.food = Food()
            self.context.increase_score()
