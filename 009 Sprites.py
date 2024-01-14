import pygame as py
from ball import Ball

py.init()
WIDTH, HEIGHT = 800, 600

WHITE=(255,255,255)
BLUE=(0,0,255)
GREEN=(0,255,0)
RED=(255,0,0)

clock = py.time.Clock()
FPS = 60
RGB = (255, 255, 255)

screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Pygame game game")
py.display.set_icon(py.image.load("icon.bmp"))


b1 = Ball(WIDTH//2,2,"img/ball.png")
b1.image = py.transform.scale(b1.image, (50, 50))

angle_ball = 0
#Основной цикл
while True:
    for event in py.event.get():
        if event.type == py.QUIT:  # закрытие игры крестиком
            exit()


    if angle_ball < 360:
        angle_ball += 1
    else:
        angle_ball = 0
    b1.rotataion(angle_ball)

    screen.fill((0,0,0))
    screen.blit(b1.image, b1.rect)
    py.display.update()

#Основной код
    b1.update(HEIGHT)


    clock.tick(FPS)  # 60 кадров в секунду