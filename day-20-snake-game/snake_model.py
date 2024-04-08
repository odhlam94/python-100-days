from turtle import Turtle, Screen
from constants import *
from time import sleep


class Snake:
    segments: list[Turtle] = []

    def __init__(self, screen: Screen):
        screen.onkey(key="d", fun=self.move_forward)
        screen.onkey(key="Up", fun=self.up_direction)
        screen.onkey(key="Right", fun=self.right_direction)
        screen.onkey(key="Left", fun=self.left_direction)
        screen.onkey(key="Down", fun=self.down_direction)
        self.screen = screen

        for position in [0, -20, -40]:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position, 0)
            self.segments.append(segment)

    @property
    def header_segment(self) -> Turtle:
        return self.segments[0]

    def play(self):
        while True:
            prev_segment = self.header_segment
            for seg in self.segments:
                # Skip with first segment
                if seg is self.header_segment:
                    continue

                prev_position = prev_segment.position()
                print(prev_position)
                seg.goto(prev_position[0], prev_position[1])
                print(prev_position[0], prev_position[1])
                prev_segment = seg
                self.header_segment.forward(DISTANCE)

            self.screen.update()
            sleep(0.1)

    def up_direction(self):
        self.header_segment.setheading(UP_DEGREE)

    def down_direction(self):
        self.header_segment.setheading(DOWN_DEGREE)

    def left_direction(self):
        self.header_segment.setheading(LEFT_DEGREE)

    def right_direction(self):
        self.header_segment.setheading(RIGHT_DEGREE)

    def move_by_direction(self, direction):
        self.header_segment.setheading(direction)

    def move_forward(self):
        self.header_segment.forward(DISTANCE)
        prev_segment = self.header_segment
        for seg in self.segments:
            # Skip with first segment
            if seg is self.header_segment:
                continue

            prev_position = prev_segment.position()
            print(prev_position)
            self.header_segment.forward(DISTANCE)
            seg.goto(prev_position[0], prev_position[1])
            prev_segment = seg

        self.screen.update()


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

