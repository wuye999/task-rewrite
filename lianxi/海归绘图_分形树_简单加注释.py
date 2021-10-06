# !/usr/bin/python3
# -*-coding:UTF-8-*-

import turtle as tt

def draw_tree(branch_length):
    '''
    绘制分形树函数
    :param branch_length:树枝的长度
    '''
    if branch_length > 5:   #画树枝，直到长度5停止
        # 里层的长度不满足"> 5"后, 就跳出回到上一层（结束条件）

        # 先绘制右侧的树枝
        tt.forward(branch_length)
        # print(f'向前 {branch_length}')
        tt.right(20)
        # print(f'右转 20')
        draw_tree(branch_length-15)

        # 再绘制左侧的树枝
        tt.left(40)
        # print(f'左转 40')
        draw_tree(branch_length-15)

        #返回之前的树枝
        tt.right(20)
        # print(f'右转 20')
        tt.backward(branch_length)
        # print(f'向后 {branch_length}')
        tt.pencolor('brown')
        tt.pensize(2)
    else:
        tt.color('green')    # 画末端
        tt.pensize(4)


def draw():
    '''
        调用绘制分形树
    '''
    # 初始化画树的位置及笔宽
    tt.left(90)
    tt.penup()
    tt.backward(200)
    tt.pendown()
    tt.pencolor('brown')
    tt.pensize(2)
    draw_tree(100)

    tt.exitonclick()

if __name__ == '__main__':
    tt.speed(10)  # 最快的速度
    draw()
    