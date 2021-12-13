import random as r

def GuessNum():
    Q1 = Q2 = 0
    for a in range(10000000) :
        Num = r.randint(0,1)
        if Num == 0:
            Q1 += 1
        else:
            Q2 += 1
    print(Q1, Q2)

GuessNum()