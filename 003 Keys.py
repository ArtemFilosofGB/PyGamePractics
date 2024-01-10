# обработка событий
# Ввод с клавиатуры

import pygame as py

WHIDTH = 800
HEIGHT = 600
screen = py.display.set_mode((WHIDTH, HEIGHT))
py.display.set_caption("Pygame game game")
py.display.set_icon(py.image.load("icon.bmp"))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

FPS = 60
clock = py.time.Clock()
x = WHIDTH // 2
y = HEIGHT // 2
speed = 10

# Основной цикл
fl_left = fl_right = fl_up = fl_down = False
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            quit()

        # Проверка когда клавиша нажимается
        elif event.type == py.KEYDOWN:
            if event.key == py.K_LEFT:
                #x -= 10
                fl_left = True
            elif event.key == py.K_RIGHT:
                #x += 10
                fl_right = True
            elif event.key == py.K_UP:
                #y -= 10
                fl_up = True
            elif event.key == py.K_DOWN:
                #y += 10
                fl_down = True
        # Проверка когда клавиша отпускается
        elif event.type == py.KEYUP:
            if event.key == py.K_LEFT:
                fl_left = False
            elif event.key == py.K_RIGHT:
                fl_right = False
            elif event.key == py.K_UP:
                fl_up = False
            elif event.key == py.K_DOWN:
                fl_down = False

    # Движение обьекта
    if fl_left:
        x -= speed
    if fl_right:
        x += speed
    if fl_up:
        y -= speed
    if fl_down:
        y += speed


    # Прорисовка обьектов
    screen.fill(WHITE)
    py.draw.rect(screen, RED, (x, y, 50, 50))
    py.display.update()

    clock.tick(FPS)