import turtle
tao = turtle.Pen() #ดึงความสามารถการใช้ปากกา
tao.shape('turtle') #เเปลงร่างเป็นเต่า
tao.color('blue')
turtle.bgcolor('black')

def  Circle() :
    '''ฟังชั้นนี้เอาไว้วาดรูปวงกลม'''
    for i in range(9) :
        tao.circle(50)
        tao.left(80)

def  Circle2() :
    '''ฟังชั้นนี้เอาไว้วาดรูปวงกลม'''
    for i in range(9) :
        tao.color('red')
        tao.circle(60)
        tao.left(80)

def  Circle3() :
    '''ฟังชั้นนี้เอาไว้วาดรูปวงกลม'''
    for i in range(9) :
        tao.color('blue')
        tao.circle(70)
        tao.left(80)


def Go(x,y) :
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

Go(-500,-100)
Circle()
tao.color('red')
Go(500,-100)
Circle()
Go(-0,200)
tao.color('green')
Circle()
Go(0,-120)
Circle()
Circle2()
Circle3()
