from turtle import Screen
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

screen = Screen()
screen.listen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)
