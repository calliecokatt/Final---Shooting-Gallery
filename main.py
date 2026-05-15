from turtle import *

### CLASS and FUNCTION DEFINITIONS ###
class Player(Turtle):
    def __init__(self, x, y, color, screen, health, right_key, left_key, alive):
        super().__init__()
        self.ht()
        self.speed(0)
        self.color(color)
        self.penup()
        self.goto(-400, 500)
        self.setheading(90)
        self.shape("turtle")
        self.bullets = []
        self.alive = True
        self.st()
        self.health = 3
        screen.onkeypress(self.turn_left, left_key)
        screen.onkeypress(self.turn_right, right_key)
        

    def turn_left(self):
        self.left(10)

    def turn_right(self):
        self.right(10)



### PROGRAM ###
screen = Screen()
screen.bgcolor("white")
screen.setup(520,720)
screen.listen()

screen.exitonclick()