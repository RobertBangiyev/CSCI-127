#Name: Robert Bangiyev
#Date: September 18th, 2018
#This program demonstrates the shades of blue
import turtle
turtle.colormode(255)
tia=turtle.Turtle()
#tia.shape("turtle")
for i in range(0,255,10):
    tia.forward(10)
    tia.pensize(i)
    tia.color(0,0,i)
