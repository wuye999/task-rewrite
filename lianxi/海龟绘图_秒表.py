from turtle import *

import time

ht()

speed(0)

penup()

goto(0, 120)

pendown()

for i in range(12):

    right(90)

    forward(10)

    backward(10)

    left(90)

    for j in range(4):

        circle(-120, 6)

        right(90)

        forward(5)

        backward(5)

        left(90)

    circle(-120, 6)

penup()

goto(0, 0)

pendown()

def pin(p, long, angle):

    p.left(90 - angle)

    p.forward(long)

def undopin(p):

    for _ in range(2):

        p.undo()

fen = clone()

miao =  clone()

miaolong = 100

fenlong = 60

miaoang = 0

fenang = 0

while True:

    pin(fen, fenlong, fenang)

    for i in range(60):

        pin(miao, miaolong, miaoang + (i * 6))

        time.sleep(0.93)

        undopin(miao)

    undopin(fen)

    fenang += 6
    