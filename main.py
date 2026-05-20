from turtle import *
import time

tracer = 0
active = True
start = time.time() 
color = ["black","red","yellow","green"]


### CLASS and FUNCTION DEFINITIONS ###
class Player(Turtle):
    def __init__(self, x, y, color, screen, shoot_key, right_key, left_key):
        super().__init__()
        self.ht()
        self.speed(0)
        self.color(color)
        self.penup()
        self.goto(x,y)
        self.setheading(90)
        self.shape("turtle")
        self.bullets = []
        self.alive = True
        self.st()
        self.health = 3
        screen.onkeypress(self.turn_left, left_key)
        screen.onkeypress(self.turn_right, right_key)
        screen.onkeypress(self.shoot, shoot_key)
      

    def turn_left(self):
        self.left(10)

    def turn_right(self):
        self.right(10)

    def shoot(self):
        bullet = Bullet(self.xcor(), self.ycor(), self.heading())
        bullets.append(bullet)

class Bullet(Turtle):
    def __init__(self, x, y, heading):
        super().__init__()
        self.shape("circle")
        self.color("black")
        self.shapesize(0.2,0.2,1)
        self.penup()
        self.goto(x,y)
        self.setheading(heading)
        self.speed = 0

    def move(self):
        self.forward(10)
        if self.xcor() > 230 or self.xcor() < -230:
            self.setheading(180 - self.heading())
        if self.ycor() > 230 or self.ycor() < -230:
            self.setheading(-self.heading())
        if self.ycor() < p1.ycor():
            self.ht()
            bullets.remove(self)


def update_block_color(block):
    colors = ["white", "red", "yellow", "green"]
    block["turtle"].color(colors[block["health"]])

def create_row(y_pos):
    row = []
    start_x = -100
    for i in range(5):
        t = Turtle()
        t.ht()
        t.shape("square")
        t.shapesize(2,2,2)
        t.color("green")
        t.speed(0)
        t.penup()
        t.goto(start_x + (i * 45), y_pos)
        block = {
            "turtle": t,
            "health": 3,
        }
        update_block_color(block)
        t.st()
        row.append(block)
    return row

def move_squares():
    for row in all_rows:
        for block in row:
            t = block["turtle"]
            t.sety(t.ycor() - 25)

### PROGRAM ###
screen = Screen()
screen.bgcolor("white")
screen.setup(520,720)
screen.listen()

bullets = []
all_rows = []
p1 = Player(-100, -150, "red",screen, "space", "d", "a")
p2 = Player(100,-150,"blue",screen, "Return", "Right","Left")

last_spawn_time = time.time()

while active:

    screen.tracer(0)
    current_time = time.time()
                  #                  this game loop is pissing me off
    if current_time - last_spawn_time > 4:
        all_rows.append(create_row(250))
        for row in all_rows:
            for block in row:
                block["turtle"].sety(block["turtle"].ycor() - 30)
        last_spawn_time = current_time

    for bullet in bullets[:]:
        bullet.move()
        for row in all_rows:
            for block in row:
                if block["health"] > 0 and bullet.distance(block["turtle"]) < 20:
                    block["health"] -= 1
                    if block["health"] <= 0:
                        block["turtle"].ht()
                    else:
                        update_block_color(block)
        
                    bullet.ht()
                    if bullet in bullets: bullets.remove(bullet)
                    break 

    screen.update()
    time.sleep(0.01)