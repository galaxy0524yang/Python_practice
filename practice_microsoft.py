# マイクロソフト ロゴ 練習

import turtle

turtle.hideturtle()
turtle.speed(100)

White = "#ffffff"
OrangeRed = "#F25022"
Green = "#7FBA00"
Blue = "#00A4EF"
Yellow = "#FFB900"

#左上
turtle.penup()
turtle.goto(-170,170)
turtle.pendown()
turtle.color(White, OrangeRed)

turtle.begin_fill()
for i in range(4):
    turtle.forward(160)
    turtle.right(90)

turtle.end_fill()

#右上
turtle.penup()
turtle.goto(5,170)
turtle.pendown()
turtle.color(White, Green)

turtle.begin_fill()
for i in range(4):
    turtle.forward(160)
    turtle.right(90)
turtle.end_fill()

#左下
turtle.penup()
turtle.goto(-170,-5)
turtle.pendown()
turtle.color(White, Blue)

turtle.begin_fill()
for i in range(4):
    turtle.forward(160)
    turtle.right(90)
turtle.end_fill()

#右下
turtle.penup()
turtle.goto(5,-5)
turtle.pendown()
turtle.color(White, Yellow)

turtle.begin_fill()
for i in range(4):
    turtle.forward(160)
    turtle.right(90)
turtle.end_fill()

# #外枠
# turtle.penup()
# turtle.goto(265,0)
# turtle.pendown()
# turtle.left(90)
# turtle.circle(265)


turtle.done()




'''
# 右下
a = 0
while a < 4:
    turtle.forward(50)
    turtle.right(90)
    a += 1

# 右上
turtle.penup()
turtle.goto(0,60)
turtle.pendown()

a = 0
while a < 4:
    turtle.forward(50)
    turtle.right(90)
    a += 1

# 左下
turtle.penup()
turtle.goto(-60,0)
turtle.pendown()

a = 0
while a < 4:
    turtle.forward(50)
    turtle.right(90)
    a += 1

# 左上
turtle.penup()
turtle.goto(-60,60)
turtle.pendown()

a = 0
while a < 4:
    turtle.forward(50)
    turtle.right(90)
    a += 1

turtle.hideturtle()

turtle.done()
'''