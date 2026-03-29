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

        self.is_attacking = False
        self.attack_time = 0

    def attack(self):
        if not self.is_attacking:
            self.is_attacking = True
            self.attack_timer = 10 

    def sword_attack(self):
        if self.is_attacking:
            if self.attack_timer == 10:
                self.sword.is_attacking = True

            self.attack_timer -= 1
            if self.attack_timer <= 0:
                self.is_attacking = False
                self.sword.is_attacking = False

    def render(self):
        pygame.draw.rect(self.screen, self.color, (self.position[0], self.position[1], self.width, self.height))

        self.sword.render(self.position, self.width, self.facing)
