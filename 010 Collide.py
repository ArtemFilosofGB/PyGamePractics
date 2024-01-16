# столкновение

# групповая обработка спрайтов

import pygame as py
from ball import Ball
from random import randint

py.init()
py.time.set_timer(py.USEREVENT, 2000)

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
background= py.transform.scale(background, (WIDTH, HEIGHT)) # масштабирование фона

score = py.image.load("img/sky.png").convert_alpha()
score = py.transform.scale(score, (100, 100))
f = py.font.SysFont("Verdana", 20)


balls_data = ({'path':'ball.png','scope':100},
            {'path':'ball2.png','scope':150},
            {'path':'ball3.png','scope':200})

ball_surf = [py.image.load('img/'+data['path']).convert_alpha() for data in balls_data]

balls = py.sprite.Group() # создание группы спрайтов для совместного управления

#вратарь
catcher = py.image.load("img/catcher.png").convert_alpha()
catcher = py.transform.scale(catcher, (200, 200))
catcher_rect = catcher.get_rect(center=(WIDTH//2, HEIGHT//2+150))
def create_ball(group):
    indx= randint(0,len(ball_surf)-1)
    x=randint(20, WIDTH-20)
    speed = randint(1, 4)

    return Ball(x, speed, ball_surf[indx],balls_data[indx]['scope'],group)


game_score = 0
def collide_balls():
    global game_score
    for ball in balls:
        if catcher_rect.collidepoint(ball.rect.center): # пересечение: координата центра мяча ball.rect.center, прямоугольник вратаря
            game_score += ball.score
            ball.kill()


speed=10#скорость вратаря
create_ball(balls)

angle_ball = 0
#Основной цикл
while True:
    for event in py.event.get():
        if event.type == py.QUIT:  # закрытие игры крестиком
            exit()

        if event.type == py.USEREVENT:
            create_ball(balls)

    keys = py.key.get_pressed()
    if keys[py.K_LEFT]:
        catcher_rect.x -= speed
        if catcher_rect.x < 0:
            catcher_rect.x = 0
    elif keys[py.K_RIGHT]:
        catcher_rect.x += speed
        if catcher_rect.x > WIDTH - catcher_rect.width:
            catcher_rect.x = WIDTH - catcher_rect.width


    collide_balls() #сначала контролируем столкновение потом прорисовываем картинку

    screen.blit(background, (0, 0))
    screen.blit(score, (0, 0))
    screen_text = f.render(str(game_score), True, (0, 0, 0))
    screen.blit(screen_text, (20, 50))
    balls.draw(screen)
    screen.blit(catcher, catcher_rect)
    py.display.update()

    #Основной код
    balls.update(HEIGHT)



    clock.tick(FPS)  # 60 кадров в секунду

# Дописать направление падения вратяря
