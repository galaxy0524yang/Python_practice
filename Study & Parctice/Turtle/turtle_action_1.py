from turtle import *

speed(1000)
hideturtle()
tracer(False)

for a in range(400):
    if a % 3 == 0:
        color("#7FBA00")
    elif a % 3 == 1:
        color("#00A4EF")
    else:
        color("#FF0000")
    forward(a)
    left(59)

done()
