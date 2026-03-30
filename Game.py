import pygame
from Environment import Environment
from Colors import COLORS

pygame.init()

SW = 1000
SH = 700

screen = pygame.display.set_mode((SW, SH))
clock = pygame.time.Clock()

class Game:
    def __init__(self):
        self.environment = Environment(screen, SW, SH)

    def action(self, keys, events):
        self.environment.action(keys, events)

    def render(self):
        screen.fill(COLORS["BACKGROUND"])

        self.environment.render()

        pygame.display.update()

        clock.tick(60)

g = Game()

while True:
    events = pygame.event.get()
    keys = pygame.key.get_pressed()

    for event in events:
        if event.type == pygame.QUIT:
            exit()

    g.action(keys, events)
    g.render()