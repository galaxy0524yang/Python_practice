# マイクロソフト ロゴ 練習
# "practice_microsoft.py" の色付きバージョン

from turtle import *

hideturtle()
speed(100)

# 色の定義
White = "#ffffff"
OrangeRed = "#F25022"
Green = "#7FBA00"
Blue = "#00A4EF"
Yellow = "#FFB900"

# 循環定義
def main(x, y, c):
    penup()
    goto(x,y)
    pendown()
    color(White, c)

    begin_fill()
    for i in range(4):
        forward(160)
        right(90)
    end_fill()

#左上
main(x=-170, y=170, c=OrangeRed)

#右上
main(x=5, y=170, c=Green)

#左下
main(x=-170, y=-5, c=Blue)

#右下
main(x=5, y=-5, c=Yellow)

done()