from turtle import Turtle
from constants import *
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()

        # Calculate boundary position
        self.x_boundary = int(X_BOUNDARY / DISTANCE) - 3
        self.y_boundary = int(Y_BOUNDARY / DISTANCE) - 3

        food = Turtle("circle")
        food.speed(0)
        food.color("green")
        food.penup()
        self.refresh()

    def refresh(self):
        rnd_x = random.randint(-self.x_boundary, self.x_boundary) * DISTANCE
        rnd_y = random.randint(-self.y_boundary, self.y_boundary) * DISTANCE
        self.goto(rnd_x, rnd_y)

