from pico2d import *

open_canvas()

boy=load_image('character.png')

def move_top():
    print('Moving top')
    for x in range(0,800,5):
        draw_boy(x,550)
    pass

def move_right():
    print('Moving right')
    for y in range(550, 50, -5):
        draw_boy(800, y)
    pass

def move_bottom():
    print('Moving bottom')
    for x in range(800, 0, -5):
        draw_boy(x, 50)
    pass

def move_left():
    print('Moving left')
    for y in range(50, 550, 5):
        draw_boy(0, y)
    pass


def move_rectangle():
    print("MOVING RECTANGLE")
    move_top()
    move_right()
    move_bottom()
    move_left()
    pass


def move_circle():
    print("MOVING CIRCLE")
    r=200
    for deg in range(0,360):
        x=r*math.cos(math.radians(deg))+400
        y=r*math.sin(math.radians(deg))+300
        draw_boy(x, y)
    pass

def move_triangle():
    print("MOVING TRIANGLE")
    x1, y1 = 400, 550
    x2, y2 = 800, 50
    x3, y3 = 0, 50
    for t in range(0, 101):
        x = x1 + (x2 - x1) * t / 100
        y = y1 + (y2 - y1) * t / 100
        draw_boy(x, y)
    for t in range(0, 101):
        x = x2 + (x3 - x2) * t / 100
        y = y2 + (y3 - y2) * t / 100
        draw_boy(x, y)
    for t in range(0, 101):
        x = x3 + (x1 - x3) * t / 100
        y = y3 + (y1 - y3) * t / 100
        draw_boy(x, y)
    pass

def draw_boy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.1)


while True:
    move_rectangle()
    move_triangle()
    move_circle()
    break
    pass


close_canvas()
