import pygame
from Sword import Sword
from Colors import COLORS

class Sprite:
    def __init__(self, screen, SW, SH, ground_position, initial_facing='right', color=COLORS["SPRITE1"]):
        self.screen = screen
        self.SW = SW
        self.SH = SH
        self.ground_position = ground_position
        self.initial_facing = initial_facing
        self.color = color

        self.current_facing = self.initial_facing

        self.width = 40
        self.height = 150

        self.position = [200 if self.initial_facing == 'right' else self.SW - self.width - 200, self.ground_position[1] - self.height]

        self.sword = Sword(self.screen)

        self.is_attacking = False
        self.attack_timer = 0
        self.allow_attack = True

        self.velocity = 10

        self.is_jumping = False

        self.velocity_y = 15
        self.gravity = 0.7

        self.health = 100
        self.health_bar_width = 200
        self.health_bar_height = 20

    def reset(self):
        self.width = 40
        self.height = 150
        self.position = [200 if self.initial_facing == 'right' else self.SW - self.width - 200, self.ground_position[1] - self.height]

        self.is_attacking = False
        self.attack_timer = 0
        self.allow_attack = True

        self.velocity = 10

        self.is_jumping = False

        self.velocity_y = 15
        self.gravity = 0.7

        self.health = 100
        self.health_bar_width = 200
        self.health_bar_height = 20

    def action(self, keys, events=None):
        if self.initial_facing == 'right':
            if keys[pygame.K_RETURN]:
                self.attack()

            if keys[pygame.K_RIGHT]:
                self.position[0] += self.velocity
                self.current_facing = 'right'
            
            if keys[pygame.K_LEFT]:
                self.position[0] -= self.velocity
                self.current_facing = 'left'

            if keys[pygame.K_DOWN]:
                self.height = 100
                self.position[1] = self.ground_position[1] - self.height

            if keys[pygame.K_UP]:
                self.is_jumping = True

        if self.initial_facing == 'left':
            if keys[pygame.K_SPACE]:
                self.attack()

            if keys[pygame.K_d]:
                self.position[0] += self.velocity
                self.current_facing = 'right'
            
            if keys[pygame.K_a]:
                self.position[0] -= self.velocity
                self.current_facing = 'left'

            if keys[pygame.K_s]:
                self.height = 100
                self.position[1] = self.ground_position[1] - self.height

            if keys[pygame.K_w]:
                self.is_jumping = True

        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.height = 150
                    self.position[1] = self.ground_position[1] - self.height
                
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    if not self.allow_attack:
                        self.allow_attack = True

    def jump(self):
        if self.is_jumping:
            self.velocity_y -= self.gravity

            self.position[1] -= self.velocity_y

            if self.position[1] + self.height >= self.ground_position[1]:
                self.is_jumping = False
                self.position[1] = self.ground_position[1] - self.height
                self.velocity_y = 15

    def attack(self):
        if not self.is_attacking and self.allow_attack:
            self.is_attacking = True
            self.attack_timer = 10 
            self.allow_attack = False

    def sword_attack(self):
        if self.is_attacking:
            if self.attack_timer == 10:
                self.sword.is_attacking = True

            self.attack_timer -= 1

            if self.attack_timer <= 0:
                self.is_attacking = False
                self.sword.is_attacking = False

    def check_boundary(self):
        if self.position[0] < 0:
            self.position[0] = 0
        elif self.position[0] + self.width > self.SW:
            self.position[0] = self.SW - self.width 

    def render(self):
        pygame.draw.rect(self.screen, self.color, (self.position[0], self.position[1], self.width, self.height))

        # health bar
        pygame.draw.rect(self.screen, self.color, (50 if self.initial_facing == 'right' else self.SW - (self.health * 2) - 50, 50, self.health * 2, self.health_bar_height))

        # health bar outline 
        pygame.draw.rect(self.screen, self.color, (50 if self.initial_facing == 'right' else self.SW - self.health_bar_width - 50, 50, self.health_bar_width, self.health_bar_height), 1)

        self.sword.render(self.position, self.width, self.current_facing)
