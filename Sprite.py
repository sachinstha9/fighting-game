import pygame
from Sword import Sword

BLUE = (0, 0, 255)

class Sprite:
    def __init__(self, screen):
        self.screen = screen

        self.width = 40
        self.height = 150

        self.position = [0, 0]

        self.facing = 'right'

        self.color = BLUE

        self.sword = Sword(self.screen)


    def render(self):
        pygame.draw.rect(self.screen, self.color, (self.position[0], self.position[1], self.width, self.height))

        self.sword.render(self.position, self.width, self.facing)
