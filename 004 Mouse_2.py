#Обработка событий мыши

import pygame as py


py.init()

screen = py.display.set_mode((1024, 800))
py.display.set_caption("Pygame game game")


py.display.set_icon(py.image.load("icon.bmp"))

clock = py.time.Clock()
FPS = 60
RGB = (255, 255, 255)


sp=None

screen.fill(RGB )
py.display.update()


while True:
    for event in py.event.get():
        if event.type == py.QUIT:  # закрытие игры крестиком
            exit()

    screen.fill(RGB)

    pos = py.mouse.get_pos()
    if py.mouse.get_focused():
        py.draw.rect(screen, (100, 100, 100), (pos[0], pos[1], 10, 10))

    pressed = py.mouse.get_pressed()
    if pressed[0]:
        if sp is None:
            sp = pos

        width = pos[0]
        height = pos[1]

        screen.fill(RGB)
        py.draw.circle(screen,(0,150,150),(pos[0],pos[1]),(pos[0]+pos[1])//2)
    else:
        sp=None
    py.display.update()

    #исчезновение курсора по нажатию кнопки мыши
    if py.mouse.get_pressed()[0]:
        py.mouse.set_visible(False)
    else:
        py.mouse.set_visible(True)
    # собственный курсор

    py.display.update()
    clock.tick(FPS)  # 60 кадров в секунду


# 6:12