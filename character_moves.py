from pico2d import *

open_canvas()

boy=load_image('character.png')


def move_rectangle():
    print("MOVING RECTANGLE")
    pass


def move_circle():
    print("MOVING CIRCLE")
    clear_canvas_now()
    boy.draw_now(400,300)
    delay(0.1)
    pass


while True:
    move_circle()
    move_rectangle()
    pass


close_canvas()
