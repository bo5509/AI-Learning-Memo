import turtle#引入库函数turtle（画图的小乌龟）
import time
import math
def drawSnake(rad, angle, len, neckrad):
    for i in range(len):
        turtle.circle(rad, angle)#画一段圆弧，半径rad（为正在起始点右边，为负在起始点左边），对应圆心角angle       
        turtle.circle(-rad, angle)
        turtle.circle(rad, angle/2)
        turtle.fd(rad)#画直线，长度：rad   
        turtle.circle(neckrad+1,180)
        turtle.fd(rad*2/3)

def drawSquare(color1, color2, lineSize, speed):
    turtle.pencolor(color1)
    turtle.pensize(lineSize)
    turtle.speed(speed)
    turtle.goto(0,0)
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.up()
    turtle.goto(-150,-120)
    turtle.pencolor(color2)
    turtle.write("Done")
    time.sleep(5)

def drawSixSquare(color1,color2,linesize,speed):
    turtle.pencolor(color1)
    turtle.pensize(linesize)
    turtle.speed(speed)
    turtle.goto(0, 0)
    for i in range(6):
        turtle.forward(100)
        turtle.right(144)
    turtle.up()
    turtle.forward(100)
    turtle.goto(-150, -120)
    turtle.pencolor(color2)
    turtle.write("Done")
    time.sleep(5)

def main():
    window = turtle.Screen()  # creat a screen
    window.bgcolor("white")
    window.title("draw something")
    turtle.setup(1300,1300,0,0)#初始化画图界面的大小1300*1300，左上角坐标（0，0）   
    pythonsize = 30
    turtle.pensize(pythonsize)#画笔大小30   
    turtle.pencolor('purple')#画笔颜色   
    turtle.seth(-40)#乌龟画笔起始方向   
    drawSnake(40,80,3,pythonsize/2)

    #drawSquare("purple","red",15,10)
    drawSixSquare("purple", "red", 15, 5)
    window.exitonclick()
#调用函数开始画图
main()