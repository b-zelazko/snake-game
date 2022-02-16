from turtle import Turtle
from random import randrange


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.respawn()

    def respawn(self):
        random_x = randrange(-300, 300, 20)
        random_y = randrange(-300, 300, 20)
        self.goto(random_x, random_y)
