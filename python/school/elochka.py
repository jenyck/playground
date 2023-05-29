#!/usr/bin/env python3
from turtle import *
from math import *

color("green")
def triangle(a):
    fillcolor("green")
    begin_fill()
    right(60)
    forward(a)
    right(120)
    forward(a)
    right(120)
    forward(a)
    right(60)
    end_fill()

def draw_green_circle(a):
    fillcolor("red")
    begin_fill()
    circle(a)
    end_fill()
    fillcolor("green")

for i in range(50, 200, 50):
    triangle(i)
    right(90)
    forward(sqrt(3)*i/4)
    right(90)
    draw_green_circle(8)
    left(90)
    pu()
    forward(sqrt(3)*i/4)
    pd()
    left(90)
