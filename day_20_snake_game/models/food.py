from turtle import Turtle, Screen
from constants import *
import random
from .shared import screen


class Food(Turtle):
    def __init__(self):
        super().__init__()
        # Calculate boundary position
        self.shape("circle")
        self.speed(0)
        self.color("green")
        self.penup()
        x_boundary = int(X_BOUNDARY / MOVE_DISTANCE) - 3
        y_boundary = int(Y_BOUNDARY / MOVE_DISTANCE) - 3
        rnd_x = random.randint(-x_boundary, x_boundary) * MOVE_DISTANCE
        rnd_y = random.randint(-y_boundary, y_boundary) * MOVE_DISTANCE
        self.goto(rnd_x, rnd_y)

    def square_transform(self):
        self.shape("square")
        self.color("white")

