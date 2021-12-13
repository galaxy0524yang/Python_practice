# 色付き MS ロゴ

import turtle as t
t.hideturtle()
t.speed(1500)
t.width(5)

# 循環関数定義
def main(c, x, y):
    t.color(c)
    t.penup()
    t.goto(x, y)
    t.pendown()

    for a in range(100):
        t.forward(a)
        t.left(90)
    for b in range(2):
        t.forward(100)
        t.left(90)
    t.forward(99)

# 左上 オレンジ
main(c="#F25022", x=-60, y=60)

# 右上 グリーン
main(c="#7FBA00", x=60, y=60)

# 左下 ブルー
main(c="#00A4EF", x=-60, y=-60)

# 左下 イエロー
main(c="#FFB900", x=60, y=-60)

t.done()
