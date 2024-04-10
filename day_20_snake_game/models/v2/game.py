from functools import partial
from turtle import Screen
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from enums import Direction, State
from .background import Background
from .snake import Snake


class SnakeGame:
    snake: Snake
    background: Background
    state: State = State.WAIT

    def __init__(self):
        # Initial screen
        screen = Screen()
        screen.listen()
        screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        screen.bgcolor('black')
        screen.title("Snake Game")
        screen.tracer(0)
        screen.onkey(key="space", fun=self.play)
        screen.onkey(key="Escape", fun=self.pause_continue)

        self.background = Background(screen)
        self.snake = Snake(screen)
        self.screen = screen

    def start(self):
        self.snake.refresh()
        self.background.display_message_by_state(self.state)
        self.screen.exitonclick()

    def play(self):
        self.state = State.PLAYING
        while self.state is State.PLAYING:
            self.snake.move()

    def pause_continue(self):
        state = State.PLAYING if self.state is State.PAUSE else State.PAUSE
        if state == State.PLAYING:
            self.play()

