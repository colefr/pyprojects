# resistor_flashgame.py
# Cole Frauzel
# 2022-03-02

# A flashcard-style game for practicing standard resistor colour codes

from random import random
from time import sleep
import turtle

colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]


def draw_rectangle(t: turtle.Turtle, corner: turtle.Vec2D, size: turtle.Vec2D, color: str):
    t.pu()
    t.pencolor("black")
    t.fillcolor(color)
    t.goto(corner)
    t.begin_fill()

    t.pd()
    t.setheading(90)
    t.forward(size[1])
    t.setheading(0)
    t.forward(size[0])
    t.setheading(270)
    t.forward(size[1])
    t.setheading(180)
    t.forward(size[0])
    t.pu()
    t.end_fill()


t = turtle.Turtle()
turtle.setup(500,200)
t.pensize(1)
t.speed(0)

# Draw some randomly generated 4-band resistors for testing
while True:
    t.clear()
    draw_rectangle(t, (-20, 20), (150, 10), "silver")
    draw_rectangle(t, (0,0), (110,50), "cyan")

    for i in range(0, 5):
        if i == 3:
            continue
        elif i == 4:
            draw_rectangle(t, (10 + i*20, 0), (10, 50), "gold")
        else:
            draw_rectangle(t, (10 + i*20, 0), (10, 50), colors[int(random() * 10)])
    
    sleep(2)