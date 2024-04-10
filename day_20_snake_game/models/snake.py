from turtle import Turtle, Screen
from time import sleep
from constants import *
from .food import Food
from .message import Message
from enums import Direction, State
from functools import partial


class Snake:
    segments: list[Turtle] = []
    __food: Food = None
    __score__: int = 0
    __state__ = State.WAIT
    high_score: int = 0

    def __init__(self, screen: Screen):
        print("Set key to control snake")
        screen.onkey(key="Up", fun=partial(self.set_heading_angle, Direction.UP_DEGREE))
        screen.onkey(key="Down", fun=partial(self.set_heading_angle, Direction.DOWN_DEGREE))
        screen.onkey(key="Right", fun=partial(self.set_heading_angle, Direction.RIGHT_DEGREE))
        screen.onkey(key="Left", fun=partial(self.set_heading_angle, Direction.LEFT_DEGREE))
        self.screen = screen
        self.food = Food()
        self.main_msg = Message("PRESS SPACE TO START", 0, 0)
        self.score_msg = Message("Score: 0  High Score: 0", 0, SCREEN_HEIGHT/2 - 50)

    def reset(self):
        if self.__state__ != State.WAIT:
            for segment in self.segments:
                segment.reset()
                segment.clear()

            self.segments = []
            self.food.clear()
            self.food.reset()

        self.__score__ = 0
        self.main_msg.clear()

    def __init_segments(self):
        for position in range(SEGMENT_LENGTH):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(-position * SEGMENT_SIZE, 0)
            segment.speed(1)
            self.segments.append(segment)

    @property
    def header_segment(self) -> Turtle:
        return self.segments[0]

    def get_state(self) -> State:
        return self.__state__

    def show_main_message(self):
        # Reset before set
        self.main_msg.clear()

        def high_score_msg():
            self.score_msg.override_msg(f"Score: {self.__score__} High Score: {self.high_score}")

        self.__show_hide_components(hide=True)

        if self.__state__ is State.GAME_OVER:
            high_score_msg()
            self.main_msg.override_msg("GAME OVER!. PRESS SPACE TO START")
        elif self.__state__ is State.PAUSE:
            high_score_msg()
            self.main_msg.override_msg("PAUSE GAME. PRESS ESCAPE TO CONTINUE")
        elif self.__state__ is State.WAIT:
            self.main_msg.override_msg("PRESS SPACE TO START")
        else:
            self.show_current_score()
            self.__show_hide_components(hide=False)

    def show_current_score(self):
        self.score_msg.clear()
        self.score_msg.override_msg(f"Score: {self.__score__}")

    def switch_state(self, state: State):
        print(f"Set state to {state}")
        self.__state__ = state
        self.high_score = max(self.high_score, self.__score__)

        if state is State.GAME_OVER:
            self.reset()

        self.show_main_message()

        if state is State.PLAYING:
            self.__play()

    def run(self):
        # Don't reset game if still playing
        if self.__state__ is State.PLAYING:
            return

        self.reset()
        self.food.refresh()
        self.__init_segments()
        self.switch_state(State.PLAYING)
        self.__play()

    def __show_hide_components(self, hide: bool):
        print("Hide component" if hide else "Show component")
        for segment in self.segments:
            segment.hideturtle() if hide else segment.showturtle()

        self.food.hideturtle() if hide else self.food.showturtle()

        self.screen.update()

    def __play(self):
        while self.__state__ == State.PLAYING:
            self.move()
            # Touch food
            if self.food.distance(self.header_segment) < 20:
                self.food.color("white")
                self.food.shape("square")
                self.segments.append(self.food)
                self.__food.refresh()
                self.__score__ += 1
                self.show_current_score()
            # Touch segment
            sleep(0.1)

    def pause(self):
        self.switch_state(State.PAUSE)
        self.__play()

    def move(self):
        segments_len = len(self.segments)
        for i in range(segments_len - 1, -1, -1):
            seg = self.segments[i]
            # First segment
            if i == 0:
                seg.forward(DISTANCE)
            else:
                front_seg = self.segments[i - 1]
                seg.goto(front_seg.xcor(), front_seg.ycor())

        for i in range(3, segments_len):
            seg = self.segments[i]
            if self.header_segment.distance(seg) < 20:
                self.switch_state(State.GAME_OVER)
                break

        self.__check_touch_boundary()

        self.screen.update()

    def set_heading_angle(self, angle: Direction):
        current_heading_angle = self.header_segment.heading()
        invert_angle = (current_heading_angle
                        + 180 if current_heading_angle <= 180 else -180)

        if invert_angle == angle.value:
            return

        self.header_segment.setheading(angle.value)

    def __check_touch_boundary(self):
        x_coord = self.header_segment.xcor()
        y_coord = self.header_segment.ycor()
        in_boundary_x = -X_BOUNDARY < x_coord < X_BOUNDARY
        in_boundary_y = -Y_BOUNDARY < y_coord < Y_BOUNDARY

        # Header touch boundary
        if not in_boundary_x or not in_boundary_y:
            x_coord = x_coord if in_boundary_x else -x_coord
            y_coord = y_coord if in_boundary_y else -y_coord
            print(f"Touched boundary. Go to position {x_coord} - {y_coord}")
            self.header_segment.goto(x_coord, y_coord)

