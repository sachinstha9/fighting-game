import pygame
from Environment import Environment

pygame.init()

SW = 1000
SH = 700

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((SW, SH))

class Game:
    def __init__(self):
        self.environment = Environment(screen, SW, SH)

    def render(self):
        screen.fill(WHITE)

        self.environment.render()

        pygame.display.update()


g = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    g.render()