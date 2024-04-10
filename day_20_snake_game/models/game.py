from turtle import Screen, Turtle
from .snake import Snake
from enums import State
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


class SnakeGame:
    screen: Screen
    snake: Snake
    
    @property
    def game_is_on(self) -> bool:
        return True

    def run(self):
        print("Running Snake Game")
        screen = Screen()
        
        self.snake = Snake(screen)
        screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        screen.bgcolor('black')
        screen.title("Snake Game")
        screen.tracer(0)

        screen.listen()
        screen.onkey(key="space", fun=self.snake.run)
        screen.onkey(key="Escape", fun=self.pause_or_continue)
        self.screen = screen
        screen.exitonclick()

    def pause_or_continue(self):
        state = State.PLAYING if self.snake.get_state() is State.PAUSE else State.PAUSE
        self.snake.switch_state(state)
        
    def draw_start_screen(self):
        pen = Turtle()
        pen.clear()
        pen.penup()
        pen.color("white")
        pen.goto(0, 100)
        pen.write("Choose Start Level", align="center", font=("Arial", 24, "normal"))
        pen.goto(0, 50)
        pen.write("Press 1, 2, or 3", align="center", font=("Arial", 18, "normal"))
        self.screen.update()

    # Function to get user input for start level
    def get_start_level(self):
        level = None
        while level not in ['1', '2', '3']:
            level = self.pen.textinput("Start Level", "Choose start level (1, 2, or 3):")
        return int(level)

