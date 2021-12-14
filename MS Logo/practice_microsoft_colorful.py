# マイクロソフト ロゴ 練習
# "practice_microsoft.py" の色付きバージョン

from turtle import *

hideturtle()
speed(100)
tracer(False)

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
main(-170, 170, OrangeRed)

#右上
main(5, 170, Green)

#左下
main(-170, -5, Blue)

#右下
main(5, -5, Yellow)

done()