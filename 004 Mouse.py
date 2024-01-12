#Обработка событий мыши

import pygame as py


py.init()

screen = py.display.set_mode((1024, 800))
py.display.set_caption("Pygame game game")


py.display.set_icon(py.image.load("icon.bmp"))

clock = py.time.Clock()
FPS = 60
RGB = (255, 255, 255)

fl_start_draw = False
start_point = end_point = False

screen.fill(RGB)
py.display.update()

while True:
    for event in py.event.get():
        if event.type == py.QUIT:  # закрытие игры крестиком
            exit()
        elif event.type == py.MOUSEBUTTONDOWN and event.button ==1: # нажата левая кнопка мыши начало рисования
            fl_start_draw = True
            start_point = event.pos
            print("Нажата левая кнопка мыши: ", event.pos)

        elif event.type == py.MOUSEMOTION:  # двигается мыш
            if fl_start_draw:
                pos = event.pos
                print("Двигается мыш: ", event.pos)

                width = pos[0] - start_point[0]
                height = pos[1] - start_point[1]

                screen.fill(RGB)
                py.draw.rect(screen,(0,0,255),(start_point[0],start_point[1],width,height))
                py.display.update()
        elif event.type == py.MOUSEBUTTONUP and event.button ==1:  # отпустили левую кнопку мыши - конец рисования
            fl_start_draw = False

    clock.tick(FPS)  # 60 кадров в секунду


# 6:12