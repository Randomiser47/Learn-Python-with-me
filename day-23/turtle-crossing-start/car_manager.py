from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# Y = [-200,-180,-150,-130,-100,-50,0,20,40,60,80,120,150,180,200]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape('square')
        self.setheading(180)
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=3)
        self.goto(320,random.choice(range(-200,200)))

    def move(self):
        self.forward(MOVE_INCREMENT)

