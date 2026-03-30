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

    def reset(self):
        self.environment.reset()

        return self.get_state()

    def get_state(self):
        return [
            self.environment.sprite1.position[0],
            self.environment.sprite1.position[1],
            self.environment.sprite1.health,
            self.environment.sprite2.position[0],
            self.environment.sprite2.position[1],
            self.environment.sprite2.health,
        ]

    def step(self, action_sprite1, action_sprite2):
        return self.get_state(), self.environment.step(action_sprite1, action_sprite2)

    def action(self, keys, events):
        self.environment.action(keys, events)

    def update(self):
        screen.fill(COLORS["BACKGROUND"])

        self.environment.update()
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
    g.update()