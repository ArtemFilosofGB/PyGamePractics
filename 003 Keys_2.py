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
    keys = py.key.get_pressed() # возвращает словарь с нажатыми клавишами и их состояниями, нет Shift Ctrl Alt
    if keys[py.K_ESCAPE]:
        py.quit()
        quit()
    if keys[py.K_LEFT]:
        x -= speed
    if keys[py.K_RIGHT]:
        x += speed
    if keys[py.K_UP]:
        y -= speed
    if keys[py.K_DOWN]:
        y += speed
    if keys[py.KMOD_CTRL]:
        speed-=10
    if keys[py.KMOD_SHIFT]:
        y+=30
        speed+=10



    # Прорисовка обьектов
    screen.fill(WHITE)
    py.draw.rect(screen, RED, (x, y, 50, 50))
    py.display.update()

    clock.tick(FPS)