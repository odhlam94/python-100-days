from functools import partial
from turtle import Turtle, Screen
from enums import Direction, State
from constants import *
from .food import Food
from .shared import screen


class Snake:
    segments: list[Turtle] = []
    screen: Screen

    def __init__(self):
        screen.onkey(key="Up", fun=partial(self.change_direction, Direction.UP_DEGREE))
        screen.onkey(key="Down", fun=partial(self.change_direction, Direction.DOWN_DEGREE))
        screen.onkey(key="Right", fun=partial(self.change_direction, Direction.RIGHT_DEGREE))
        screen.onkey(key="Left", fun=partial(self.change_direction, Direction.LEFT_DEGREE))

    def refresh(self):
        for segment in self.segments:
            segment.clear()
            segment.reset()
            segment.hideturtle()
        self.segments.clear()

        # Init snake segments
        for position in range(SEGMENT_LENGTH):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(-position * SEGMENT_SIZE, 0)
            segment.speed("slowest")
            self.segments.append(segment)

    @property
    def head(self) -> Turtle:
        return self.segments[0]

    def change_direction(self, angle: Direction):
        """Change direction of movement include UP, DOWN, LEFT, RIGHT"""
        current_heading_angle = self.head.heading()
        invert_angle = (current_heading_angle
                        + 180 if current_heading_angle <= 180 else -180)

        if invert_angle == angle.value:
            return

        self.head.setheading(angle.value)

    def move(self) -> State:
        """
        Keep move forward for snack
        If Snake touched boundary --> Game over!
        """
        segments_len = len(self.segments) - 1
        for i in range(segments_len, -1, -1):
            seg = self.segments[i]
            # First segment
            if i == 0:
                seg.forward(MOVE_DISTANCE)
                self.__check_touch_boundary()
            else:
                front_seg = self.segments[i - 1]
                seg.goto(front_seg.xcor(), front_seg.ycor())

        for seg in self.segments[3:segments_len]:
            if self.head.distance(seg) < 20:
                return State.GAME_OVER

        # self.__check_touch_boundary()
        screen.update()
        return State.PLAYING

    def __check_touch_boundary(self):
        x_coord = self.head.xcor()
        y_coord = self.head.ycor()
        in_boundary_x = -X_BOUNDARY < x_coord < X_BOUNDARY
        in_boundary_y = -Y_BOUNDARY < y_coord < Y_BOUNDARY

        # Header touch boundary
        if not in_boundary_x or not in_boundary_y:
            x_coord = x_coord if in_boundary_x else -x_coord
            y_coord = y_coord if in_boundary_y else -y_coord
            print(f"Touched boundary. Go to position {x_coord} - {y_coord}")
            self.head.goto(x_coord, y_coord)

    def extend(self, food: Food):
        # Transform segment before append
        food.square_transform()
        self.segments.append(food)
