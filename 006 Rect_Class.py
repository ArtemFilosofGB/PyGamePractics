# Rect
import pygame as py

py.init()
WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

clock = py.time.Clock()
FPS = 60
RGB = (255, 255, 255)

screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Pygame game game")
py.display.set_icon(py.image.load("icon.bmp"))

ground = HEIGHT - 70
jump_force = 20  # сила прыжка
move = jump_force + 1  # текущая вертикальная скорость

# Hero
hero = py.Surface((40, 50))
hero.fill(BLUE)
rect = hero.get_rect(center=(WIDTH // 2, HEIGHT // 2))
rect.bottom = ground  # hero будет поставлен на землю
#обновление rect отдельно

rect_update = py.Rect(rect.x,0,rect.width,ground)

# print(rect)
# print(type(rect))

# screen.fill(WHITE)
# screen.blit(hero, rect)
# # screen.blit(hero, (100, 100))
# py.display.update()

# Совмещение поверхностей
# rect1 = py.Rect(0, 0, 30, 30)
# rect2 = py.Rect(30, 30, 30, 30)
#
# rect2.move_ip(20,20)
# print(rect2) #<rect2 (50, 50, 30, 30)>
#
# rect3=rect2.union(rect1)
# print(rect3) # <rect(0, 0, 80, 80)>

screen.fill(WHITE)
py.display.update()

# Основной цикл
while True:
    for event in py.event.get():
        if event.type == py.QUIT:  # закрытие игры крестиком
            exit()

        elif event.type == py.KEYDOWN:
            if event.key == py.K_SPACE and ground == rect.bottom:
                move = -jump_force
    # отработка прыжка
    if move <= jump_force:
        if rect.bottom + move < ground:
            rect.bottom += move
            if move <jump_force:
                move += 1
        else:
            rect.bottom = ground
            move = jump_force + 1
    screen.fill(WHITE)
    screen.blit(hero, rect)
    py.display.update(rect_update) # обновление rect отдельно, только той области где происходит прыжок


    clock.tick(FPS)  # 60 кадров в секунду

# 11:44
