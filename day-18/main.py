import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = [
    "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
    "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"
]

directions = [0, 90, 180, 270]

while True:
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(range(0, 360)))

