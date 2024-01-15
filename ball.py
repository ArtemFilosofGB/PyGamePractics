import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self,x, speed_fall, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        #self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speed_fall


    def update(self,*args):
        if self.rect.y < args[0]-20:
            self.rect.y+=self.speed
        else:
            self.rect.y = 0
        # Вращение мяча


