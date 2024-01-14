import pygame as py

py.init()
print(py.font.get_fonts())  # ['arial', 'arialblack', 'bahnschrift', 'calibri', 'cambria', 'cambriamath'...

f_sys = py.font.SysFont("Arial", 30)  # загрузка предустановленного шрифта
f1 = py.font.Font('fonts/PixeloidMono.ttf', 24)  # загрузка отдельного шрифта
f2 = py.font.Font('fonts/PixeloidSans.ttf', 24)
f3 = py.font.Font('fonts/PixeloidSans-Bold.ttf', 24)

WIDTH, HEIGHT = 800, 600

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

def text_board():
    sc_text1 = f1.render("Hello, World!", 1, RED)  # render формирует поверхность на которой пишется текст, 1- сглаженный
    pos = sc_text1.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(sc_text1, pos)

    sc_text2 = f2.render("Hello, World!", 1, RED)  # render формирует поверхность на которой пишется текст, 1- сглаженный
    pos2 = sc_text2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))
    screen.blit(sc_text2, pos2)

    sc_text3 = (f3.render("Hello, World!", 1, RED))  # render формирует поверхность на которой пишется текст, 1- сглаженный
    pos3 = sc_text3.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))
    screen.blit(sc_text3, pos3)
    py.display.update()

f = py.font.SysFont(None, 50)
sc_text = f.render("Принветики", 0, BLUE)
pos = sc_text.get_rect(center=(WIDTH // 2 - 100, HEIGHT // 2 - 100))

def draw_text():
    screen.fill(WHITE)
    screen.blit(sc_text, pos)
    py.display.update()

draw_text()

while 1:
    for event in py.event.get():
        if event.type == py.QUIT:  # закрытие игры крестиком
            exit()
        elif event.type == py.MOUSEBUTTONDOWN and event.button == 1: #нажата 1 кнопка мыши
            py.mouse.get_rel()#обнуляем первое смещение при повторном вызове

    #перемещение
    if py.mouse.get_focused() and pos.collidepoint(py.mouse.get_pos()):
        btns = py.mouse.get_pressed()
        if btns[0]:
            rel = py.mouse.get_rel() #получаем последующие смещения
            pos.move_ip(rel)
            draw_text()

            text_board()

    clock.tick(FPS)
