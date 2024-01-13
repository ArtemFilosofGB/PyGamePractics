# Поверхности

import pygame as py

py.init()
WIDTH, HEIGHT = 800, 600

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

clock = py.time.Clock()
FPS = 60
RGB = (255, 255, 255)

# Screen
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Pygame game game")
py.display.set_icon(py.image.load("icon.bmp"))
screen.fill(WHITE)

# #Surf
# surf = py.Surface((200, 200))
# surf.fill(RED)
# py.draw.circle(surf, GREEN, (100, 100), 80)
#
# #Surf_alpha
# surf_alpha = py.Surface((WIDTH, 100))
# py.draw.rect(surf_alpha, BLUE, (0, 0, WIDTH, 100))
# surf_alpha.set_alpha(128)
#
# # наложение поверхностей
# # поверхность surf отображается в screen с координатами (50, 50)
# surf.blit(surf_alpha, (0, 50))# поверхность surf_alpha отображается в surf с координатами (0, 50)
# screen.blit(surf, (50, 50))

surf = py.Surface((WIDTH, 200))
bita = py.Surface((50, 50))

surf.fill(BLUE)
bita.fill(RED)
bita.set_alpha(0)

bx, by = 0, 150
x, y = 0, 0

py.display.update()

# Основной цикл
while True:
    for event in py.event.get():
        if event.type == py.QUIT:  # закрытие игры крестиком
            exit()
    # Отрисовка поверхностей
    surf.fill(BLUE)
    surf.blit(bita, (bx, by))
    bita.set_alpha(int(255-bx//3.2)) # изменение прозрачности 0 .. 250
    print(bx)
    #Измененние координат поверхностей
    if bx<WIDTH:
        bx+=5
    else:
        bx=0
    if y<HEIGHT:
        y+=1
    else:
        y=0
    screen.fill(WHITE)
    screen.blit(surf, (x, y))

    #движение на клавиатуре
    if event.type == py.KEYDOWN:
        if event.key == py.K_LEFT:
            x-=10
        elif event.key == py.K_RIGHT:
            x+=10
        elif event.key == py.K_UP:
            y-=10
        elif event.key == py.K_DOWN:
            y+=10

    py.display.update()
    clock.tick(FPS)  # 60 кадров в секунду

# 4:23
