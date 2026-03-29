import pygame
import Sword
import Sprite

pygame.init()

SW = 1000
SH = 800

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((SW, SH))

class Environment:
    def __init__(self):
        pass

    def render(self):
        pass

g = Environment()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    g.render()