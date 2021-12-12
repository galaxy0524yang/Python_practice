# 色付き MS ロゴ
# 関数を定義しましょう。
import turtle as t
t.hideturtle()
t.speed(150)

# 左上 オレンジ

t.color("#F25022")
t.width(10)
t.penup()
t.goto(-110,110)
t.pendown()

for a in range(10):
    t.forward(100)
    if a % 2 == 0:
        t.right(90)
        t.forward(10)
        t.right(90)
    else:
        t.left(90)
        t.forward(10)
        t.left(90)

t.forward(100)

for b in range(3):
    t.left(90)
    t.forward(100)

# 右上 グリーン

t.color("#7FBA00")
t.width(10)
t.penup()
t.goto(10,110)
t.pendown()
t.left(90)

for a in range(10):
    t.forward(100)
    if a % 2 == 0:
        t.right(90)
        t.forward(10)
        t.right(90)
    else:
        t.left(90)
        t.forward(10)
        t.left(90)

t.forward(100)

for b in range(3):
    t.left(90)
    t.forward(100)

# 左下 ブルー

t.color("#00A4EF")
t.width(10)
t.penup()
t.goto(-110,-10)
t.pendown()
t.left(90)

for a in range(10):
    t.forward(100)
    if a % 2 == 0:
        t.right(90)
        t.forward(10)
        t.right(90)
    else:
        t.left(90)
        t.forward(10)
        t.left(90)

t.forward(100)

for b in range(3):
    t.left(90)
    t.forward(100)

# 左下 イエロー

t.color("#FFB900")
t.width(10)
t.penup()
t.goto(10,-10)
t.pendown()
t.left(90)

for a in range(10):
    t.forward(100)
    if a % 2 == 0:
        t.right(90)
        t.forward(10)
        t.right(90)
    else:
        t.left(90)
        t.forward(10)
        t.left(90)

t.forward(100)

for b in range(3):
    t.left(90)
    t.forward(100)

t.done()