import pygame

BLACK = (0, 0, 0)

class Player:
    def __init__(self, screen):
        self.screen = screen

        self.width = 40
        self.height = 40

        self.position = [0, 0]

    def render(self):
        self.screen.fill(BLACK)
        pygame.display.update()
