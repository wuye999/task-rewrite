from turtle import Turtle,done,colormode,setup,title

from random import randint,uniform

title('给我一点时间，还你一棵树')

colormode(255)      #设置画笔颜色模式，为随机生成RGB色彩做准备

p1 = Turtle()       #实例化一个画笔

p1.width(20)       #设置画笔宽度，初始宽度，主树干宽度

p1.speed(100)      #设置画笔速度，具体是多少最快，查阅一下

p1.pencolor(randint(0,254),randint(0,254),randint(0,254))      #初始画笔颜色,这是随机颜色，可以用0,0,0,表示黑色

p1.hideturtle()    #隐藏画笔外形

l = 150   #初始树干长度

s = 45    #侧枝生长角度  ，这里可以改，观察生长状态

p1.lt(90)          #默认画笔在画布正中央，方向向右，lt(90)调整为向上。

p1.penup()         #提起画笔，以便直接调整画笔位置，移动路径画布上没有痕迹

p1.bk(l)           #向后（向下）移动，调整树干起点

p1.pendown()       #落下画笔，可以继续画

p1.fd(l)           #画主树干

plist = [p1]       #列表化画笔，便于树干分支控制

def draw_tree(plist,l,s,level):      #参数level为分支层数，数值越大分支越多，相对画的时间也越长。

    l = l*uniform(0.7,0.8)           #分支树干为上一个的随机比例，这里可以改

    for p1 in plist:

        w = p1.width()

        p1.width(w*3/4)

        p1.pencolor(randint(0,254),randint(0,254),randint(0,254))

        p2 = p1.clone()

        p1.lt(s)

        p1.fd(l)

        p2.rt(s)

        p2.fd(l)

        lst = []

        lst.append(p1)

        lst.append(p2)

        if level > 0:

            draw_tree(lst,l,s,level-1)

draw_tree(plist,l,s,5)

done()
