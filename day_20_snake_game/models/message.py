from turtle import Turtle


class Message(Turtle):
    def __init__(self, msg, x, y):
        super().__init__()
        self.speed(0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(msg, align="center", font=("Arial", 24, "normal"))

    def override_msg(self, msg):
        self.clear()
        self.write(msg, align="center", font=("Arial", 24, "normal"))
