import turtle
tia=turtle.Turtle()
names=["violet", "purple", "indigo", "lavender"]
for c in names:
    tia.color(c)
    tia.left(60)
    tia.forward(40)
    tia.dot(10)

tia.penup()
tia.forward(100)
tia.pendown()

for i in names:
    tia.color(i)
    tia.left(60)
    tia.forward(40)
    tia.dot(10)
