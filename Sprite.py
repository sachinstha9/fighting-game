import pygame
from Sword import Sword
from Colors import COLORS

class Sprite:
    def __init__(self, screen, SW, SH, ground_position, facing='right', color=COLORS["SPRITE1"]):
        self.screen = screen
        self.SW = SW
        self.SH = SH
        self.ground_position = ground_position
        self.facing = facing
        self.color = color

        self.width = 40
        self.height = 150

        self.position = [100 if facing == 'right' else self.SW - self.width - 100, self.ground_position[1] - self.height]

        self.sword = Sword(self.screen)

    def render(self):
        pygame.draw.rect(self.screen, self.color, (self.position[0], self.position[1], self.width, self.height))

        self.sword.render(self.position, self.width, self.facing)
