import pygame as py
import math
print(py.image.get_extended()) #True (1) можно использовать JPEG PNG если 0 то только BMP

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



#загрузка фона
background= py.image.load(("img/sky.png")).convert()
#background.convert() # метод поверхнгости будет более быстрым
background= py.transform.scale(background, (WIDTH, HEIGHT)) # масштабирование фона

# загрузка героя
hero = py.image.load("img/hero.png") # поверхность на которой будет нанесён hero.png
hero.convert_alpha()
hero.set_colorkey((255, 255, 255)) # убираем белый фон

#проеобразование героя

hero_up = hero
hero_down=py.transform.flip(hero, False, True) # зеркальное отображение по оси х
hero_down.set_colorkey((255, 255, 255))
hero_left=py.transform.rotate(hero, 90)
hero_left.set_colorkey((255, 255, 255))
hero_right=py.transform.rotate(hero, -90)
hero_right.set_colorkey((255, 255, 255))

hero_rect = hero.get_rect(center=(WIDTH//2, HEIGHT//2))
hero.set_colorkey((255, 255, 255))


bird = py.image.load("img/bird.png")
bird.convert()
bird_small=py.transform.scale(bird, (50, 50))
#bird_small=py.transform.rotate(bird_small, 180)
bird_small = py.transform.flip(bird_small, 1, 0)
bird_small.set_colorkey((255, 255, 255))



#порядов вывода слоёв
screen.blit(background, (0, 0))
screen.blit(hero, (50, 50))
bird_x=0
brd_y=0


hero_now=hero_up
spped=5

py.display.update()

#Основной цикл
while True:
    for event in py.event.get():
        if event.type == py.QUIT:  # закрытие игры крестиком
            exit()

    bt=py.key.get_pressed()
    if bt[py.K_LEFT]:
        print("left")
        hero_now=hero_left
        hero_rect.x-=spped
        if hero_rect.x<0:
            hero_rect.x=0
    elif bt[py.K_RIGHT]:
        print("right")
        hero_now=hero_right
        hero_rect.x+=spped
        if hero_rect.x>WIDTH-hero_rect.width:
            hero_rect.x=WIDTH-hero_rect.width
    elif bt[py.K_UP]:
        print("up")
        hero_now=hero_up
        hero_rect.y-=spped
        if hero_rect.y<0:
            hero_rect.y=0
    elif bt[py.K_DOWN]:
        print("down")
        hero_now=hero_down
        hero_rect.y+=spped
        if hero_rect.y>HEIGHT-hero_rect.height:
            hero_rect.y=HEIGHT-hero_rect.height
    if bird_x>WIDTH:
        bird_x=0
        brd_y=math.sin(math.radians(bird_x))*100+100
    else:
        bird_x+=5
        brd_y=math.sin(math.radians(bird_x))*100+100
    screen.blit(background, (0, 0))
    screen.blit(bird_small, (bird_x, brd_y))
    screen.blit(hero_now, hero_rect)

    py.display.update()


#Основной код



    clock.tick(FPS)  # 60 кадров в секунду