import pygame
from Colors import COLORS

class Sword:
    def __init__(self, screen):
        self.screen = screen

        self.width = 10
        self.height = 100

        self.color = COLORS["SWORD"]

        self.position = [0, 0]

        self.isAttacked = False

    def render(self, sprite_position, spite_width, sprite_facing='right'):
        x_shift = 10
        y_shift = 60

        if sprite_facing == 'right':
            self.position[0] = sprite_position[0] + x_shift
        else:
            self.position[0] = sprite_position[0] + spite_width - x_shift - self.width
        
        self.position[1] = sprite_position[1] - y_shift

        pygame.draw.rect(self.screen, self.color, (self.position[0], self.position[1], self.width, self.height))