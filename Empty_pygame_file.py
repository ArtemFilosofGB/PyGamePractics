import pygame as py

py.init()

screen = py.display.set_mode((1024, 800))
py.display.set_caption("Pygame game game")
py.display.set_icon(py.image.load("icon.bmp"))

clock = py.time.Clock()
FPS = 60
RGB = (255, 255, 255)

#Основной цикл
while True:
    for event in py.event.get():
        if event.type == py.QUIT:  # закрытие игры крестиком
            exit()

#Основной код



    clock.tick(FPS)  # 60 кадров в секунду