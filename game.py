import pygame

pygame.init()

SW = 1000
SH = 800

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SW, SH))

g = Game()
