#Robert Bangiyev
#November 14, 2018
#This program makes a turtle go randomly
import turtle
import random

tom = turtle.Turtle()
tom.speed(10)
for i in range(100):
    tom.forward(10)
    a = random.randrange(0,360,1)
    tom.right(a)
