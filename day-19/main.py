from turtle import Turtle, Screen

screen = Screen()
tim  = Turtle()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_left():
    tim.left(90)


def turn_right():
    tim.right(90)


tim.speed('slowest')

screen.setup(width=500, height=400)
screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="d", fun=move_backward)

screen.exitonclick()
