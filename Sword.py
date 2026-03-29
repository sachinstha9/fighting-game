import pygame

RED = (255, 0, 0)

class Sword:
    def __init__(self, screen):
        self.screen = screen

        self.width = 10
        self.height = 50

        self.color = RED

        self.position = [0, 0]

        self.isAttacked = False

    def render(self):
        pygame.draw.rect(self.screen, self.color, (self.position[0], self.position[1], self.width, self.height))
