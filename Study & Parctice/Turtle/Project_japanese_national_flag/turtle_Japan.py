# 日本国旗
from turtle import *

# turtle プロパティ設定
length = 1200
height = 800
setup(length, height)
hideturtle()
tracer(False)

# 白い部分
penup()
goto(-375,250)
pendown()
color("#000000", "#ffffff")

begin_fill()
forward(750)
right(90)
forward(500)
right(90)
forward(750)
right(90)
forward(500)
end_fill()

# 真ん中の赤い円
penup()
goto(150, 0)
pendown()
color("#FF0000","#FF0000")

begin_fill()
circle(150)
end_fill()

# ts = getscreen()
# ts.getcanvas().postscript(file = r"C:/PythonProjects/Python_Practice/Study & Parctice/Turtle/日本国旗.eps")

done()