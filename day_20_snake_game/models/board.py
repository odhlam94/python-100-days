from turtle import Turtle


class Board(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.speed(0)
        self.color("white")
        self.penup()
        self.goto(x, y)
        self.hideturtle()

    def overwrite(self, msg):
        self.clear()
        self.write(msg, align="center", font=("Arial", 24, "normal"))
