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

background= py.image.load(("img/sky.png")).convert()
background.convert() # метод поверхнгости будет более быстрым
background= py.transform.scale(background, (WIDTH, HEIGHT)) # масштабирование фона

balls = py.sprite.Group() # создание группы спрайтов для совместного управления

balls.add(Ball(WIDTH//2,2,"img/ball.png"))
balls.add(Ball(WIDTH//2+100,3,"img/ball2.png"), Ball(WIDTH//2-100,5,"img/ball3.png"))


# b1 = Ball(WIDTH//2,2,"img/ball.png")
# b2 = Ball(WIDTH//2+100,3,"img/ball2.png")
# b3 = Ball(WIDTH//2-100,5,"img/ball3.png")




angle_ball = 0
#Основной цикл
while True:
    for event in py.event.get():
        if event.type == py.QUIT:  # закрытие игры крестиком
            exit()

    screen.blit(background, (0, 0))
    balls.draw(screen)

    py.display.update()

#Основной код
    balls.update(HEIGHT)



    clock.tick(FPS)  # 60 кадров в секунду