import turtle           #'turtle'モジュールを導入する
turtle.showturtle()     #シャトルを表示する
turtle.color("blue")    #色を指定する
turtle.speed(1)    #'turtle'モジュールの速度

turtle.write("START !") #文字を入れる
turtle.forward(300)     #前に300単位進む

turtle.left(90)         #左90度に曲がる
turtle.forward(300)
turtle.left(135)
turtle.goto(0,0)        #'0,0'の所へ行く
turtle.right(135)
turtle.goto(0,300)
turtle.right(90)
turtle.goto(300,300)

turtle.left(135)
turtle.circle(212.1)    #円を描く

turtle.done()           #終了