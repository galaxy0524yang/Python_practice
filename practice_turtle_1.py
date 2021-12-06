import turtle
import math

#点を定義する
x1,y1 = 100,100
x2,y2 = 100,-100
x3,y3 = -100,-100
x4,y4 = -100,100

# 'turtle'で線を引く
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()

turtle.goto(x2,y2)
turtle.goto(x3,y3)
turtle.goto(x4,y4)


# スタート位置から終了位置までの距離計算
distance = math.sqrt((x1-x4)**2 + (y1-y4)**2)

turtle.write(distance)
