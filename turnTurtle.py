#Name: Robert Bangiyev
#Date: October 3, 2018
#This program asks the user to input a number and then makes the turtle turn
import turtle
tom=turtle.Turtle()
for i in range(5):
    num=int(input("Enter a number: "))
    tom.left(num)
    tom.forward(100)
