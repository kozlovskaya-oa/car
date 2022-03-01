import os
import sys

import pygame


pygame.init()
size = width, height = 600, 95
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Car')


def load_image(name, colorkey=None):
    fullname = os.path.join("data", name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


all_sprites = pygame.sprite.Group()


class Car(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites)
        self.image = load_image("car.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.direct = 1
        self.start = 1

    def update(self):
        if self.rect.x == 450:
            self.direct *= -1
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect.x += self.direct
        elif self.rect.x == 0:
            if self.start:
                self.rect.x += self.direct
                self.start = False
            else:
                self.direct *= -1
                self.image = pygame.transform.flip(self.image, True, False)
                self.rect.x += self.direct
        else:
            self.rect.x += self.direct


scr = Car(0, 0)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(60)
