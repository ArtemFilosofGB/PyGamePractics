# Поверхности

import pygame as py
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


surf = py.Surface((200, 200))
surf.fill(RED)
py.draw.circle(surf, GREEN, (100, 100), 80)

surf_alpha = py.Surface((WIDTH, 100))
py.draw.rect(surf_alpha, BLUE, (0, 0, WIDTH, 100))
surf_alpha.set_alpha(128)



# наложение поверхностей
# поверхность surf отображается в screen с координатами (50, 50)
surf.blit(surf_alpha, (0, 50))# поверхность surf_alpha отображается в surf с координатами (0, 50)
screen.blit(surf, (50, 50))
py.display.update()

#Основной цикл
while True:
    for event in py.event.get():
        if event.type == py.QUIT:  # закрытие игры крестиком
            exit()

#Основной код



    clock.tick(FPS)  # 60 кадров в секунду


#4:23