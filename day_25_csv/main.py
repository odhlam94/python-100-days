import turtle

screen = turtle.Screen()
screen.setup(725, 491)
screen.bgpic('blank_states_img.gif')
screen.title('U.S States Game')


def screen_click(x, y):
    print(x, y)


turtle.onscreenclick(screen_click)

turtle.mainloop()
