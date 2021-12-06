#五輪を絵描く

import turtle

turtle.width(10)

turtle.color("blue")
# turtle.write("(0,0)")
turtle.circle(50)

turtle.penup()
turtle.goto(120,0)
turtle.color("black")
# turtle.write("(120,0)")

turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.goto(240,0)
turtle.color("red")
# turtle.write("(240,0)")

turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.goto(60,-50)
turtle.color("yellow")
# turtle.write("(60,-50)")

turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.goto(180,-50)
turtle.color("green")
# turtle.write("(180,-50)")

turtle.pendown()
turtle.circle(50)

turtle.done()