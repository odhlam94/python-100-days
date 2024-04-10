from turtle import Screen
from .snake import Snake


class SnakeGame:
    screen: Screen

    @property
    def game_is_on(self) -> bool:
        return True

    def run(self):
        print("Running SnakeGame")
        screen = Screen()
        snake = Snake(screen)

        screen.setup(width=600, height=600)
        screen.bgcolor('black')
        screen.title("Snake Game")
        screen.tracer(0)

        screen.listen()
        print("Set press enter key to start a new game")
        # screen.onkey(key="space", fun=snake.play)
        screen.exitonclick()

        self.screen = screen
