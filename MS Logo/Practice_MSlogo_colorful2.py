# 色付き MS ロゴ

import turtle as t
t.hideturtle()
t.speed(1500)
t.width(5)

# 左上 オレンジ

t.color("#F25022")
t.penup()
t.goto(-60,60)
t.pendown()

for x in range(100):
    t.forward(x)
    t.left(90)
for a in range(2):
    t.forward(100)
    t.left(90)
t.forward(99)


# 右上 グリーン

t.color("#7FBA00")
t.penup()
t.goto(60,60)
t.pendown()

for x in range(100):
    t.forward(x)
    t.left(90)
for a in range(2):
    t.forward(100)
    t.left(90)
t.forward(99)

# 左下 ブルー

t.color("#00A4EF")
t.penup()
t.goto(-60,-60)
t.pendown()

for x in range(100):
    t.forward(x)
    t.left(90)
for a in range(2):
    t.forward(100)
    t.left(90)
t.forward(99)

# 左下 イエロー

t.color("#FFB900")
t.penup()
t.goto(60,-60)
t.pendown()

for x in range(100):
    t.forward(x)
    t.left(90)
for a in range(2):
    t.forward(100)
    t.left(90)
t.forward(99)

t.done()
