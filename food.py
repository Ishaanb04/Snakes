from turtle import Turtle
import random

MAX_DISTANCE_X = -23
MAX_DISTANCE_Y = 23


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('red')
        self.speed(10)
        self.refresh()

    def reset(self):
        self.refresh()

    def refresh(self):
        self.goto(random.randint(MAX_DISTANCE_X, MAX_DISTANCE_Y) * 10, random.randint(MAX_DISTANCE_X, MAX_DISTANCE_Y) * 10)
