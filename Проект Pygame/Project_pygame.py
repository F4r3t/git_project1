import os
import sys

import pygame

pygame.init()
SIZE = WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('flash car')


def load_image(name, colorkey=None):
    fullname = os.path.join('cache', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Menu:
    pass


class Game:
    pass


class Road(Game):
    pass


class Car(pygame.sprite.Sprite):
    pass


class Stone(pygame.sprite.Sprite):
    pass


class GameOver:
    pass


if __name__ == '__main__':
    pass