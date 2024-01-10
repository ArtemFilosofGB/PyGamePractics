import pygame as py
import pygame

pygame.init()

screen = pygame.display.set_mode((1024, 800))
pygame.display.set_caption("Pygame game game")


pygame.display.set_icon(pygame.image.load("icon.bmp"))

gamerun = True
clock = pygame.time.Clock()
FPS = 60
RGB = (255, 255, 255)


while gamerun == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # закрытие игры крестиком
            pygame.quit()
            gamerun = False

    for r in range(10):
        for g in range(10):
            for b in range(10):
                py.draw.ellipse(screen, (r*10, g*10, b*10), (10+r*10, 10+g*10, 100, 100),2)
                py.display.update()
    for r in range(10):
        for g in range(10):
            for b in range(10):
                py.draw.line(screen, (r*10,g*10,b*10), (100+r*10*2, 100+g*10*2), (200+r*10*2, 200+g*10*2),5)
                py.display.update()
                py.draw.aaline(screen,(r*10,g*10,b*10),(300+r*10, 300+g*10),(400+r*10, 400+g*10))
                py.display.update()
    for r in range(10):
        for g in range(10):
            for b in range(10):
                py.draw.circle(screen, (r*10,g*10,b*10), (400+r*10, 400+g*10), 10)
                py.draw.lines(screen, (r*10,g*10,b*10), False, [(500+r*10, 500+g*10), (600+r*10, 600+g*10), (800+r*10, 800+g*10)])
                py.display.update()
    for r in range(10):
        for g in range(10):
            for b in range(10):
                py.draw.polygon(screen, (r*10,g*10,b*10), [(100+r*10, 100+g*10), (200+r*10, 200+g*10), (900+r*10, 900+g*10)])
                py.draw.arc(screen, (r*10,g*10,b*10), ((100+r*10, 100+g*10), (200+r*10, 200+g*10)), 0, 3.14)
                py.display.update()



    # pygame.time.delay(20) # задержка на 20 миллисекунд
    clock.tick(FPS)  # 60 кадров в секунду


