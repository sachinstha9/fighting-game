import pygame
from Sprite import Sprite
from Colors import COLORS

class Environment:
    def __init__(self, screen, SW, SH):
        self.screen = screen

        self.ground_width = SW
        self.ground_height = 200

        self.ground_position = [0, SH - self.ground_height]

        self.sprite1 = Sprite(screen, SW, SH, self.ground_position, 'right', COLORS["SPRITE1"])
        self.sprite2 = Sprite(screen, SW, SH, self.ground_position, 'left', COLORS["SPRITE2"])

        self.ground_color = COLORS["GROUND"] 

        self.sprite1_attack = False
        self.sprite2_attack = False

    def action(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.sprite1.attack()

    def render(self):
        self.sprite1.render()
        self.sprite2.render()

        self.sprite1.sword_attack()

        pygame.draw.rect(self.screen, self.ground_color, (self.ground_position[0], self.ground_position[1], self.ground_width, self.ground_height))


