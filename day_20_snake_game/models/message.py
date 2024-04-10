from turtle import Turtle


class Pen:
    def __init__(self):
        pen = Turtle("square")
        pen.speed(0)
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        self.pen = pen

    def write(self, x, y, msg: str, align="center", font=("Courier", 24, "normal")):
        self.pen.goto(x, y)
        self.pen.write(msg, align=align, font=font)
